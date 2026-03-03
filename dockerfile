# ==============================================================================
# 1. IMAGE DE BASE
# ==============================================================================
FROM python:3.12-slim

WORKDIR /app

# ==============================================================================
# 2. INSTALLATION DU MOTEUR (uv)
# ==============================================================================
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# ==============================================================================
# 3. CRÉATION DE L'INFRASTRUCTURE DE LOGS
# ==============================================================================
# On crée le dossier AVANT de copier le code pour bien séparer les couches
RUN mkdir -p /app/logs

# ==============================================================================
# 4. GESTION DES DÉPENDANCES ET CODE
# ==============================================================================
COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev --frozen

COPY app/ ./app/

# ==============================================================================
# 5. SÉCURISATION (Moindre Privilège)
# ==============================================================================
# NOUVEAU : On crée un utilisateur système sans privilèges pour exécuter l'app
RUN useradd --create-home appuser
# On donne les droits du dossier logs à ce nouvel utilisateur
RUN chown -R appuser:appuser /app/logs
# On bascule sur cet utilisateur pour le reste de l'exécution
USER appuser

# ==============================================================================
# 6. PERSISTENCE ET LANCEMENT
# ==============================================================================
VOLUME /app/logs

# NOUVEAU : On ajoute l'environnement virtuel d'uv au PATH
# Cela évite d'appeler `uv run` à chaque démarrage du conteneur (plus rapide et standard)
ENV PATH="/app/.venv/bin:$PATH"

# On appelle directement python
CMD ["python", "app/main.py"]