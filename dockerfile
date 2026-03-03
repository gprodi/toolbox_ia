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
# 5. PERSISTENCE (Optionnel mais recommandé)
# ==============================================================================
# Indique à Docker que ce dossier est destiné à être monté en volume
VOLUME /app/logs

CMD ["uv", "run", "--no-dev", "python", "app/main.py"]