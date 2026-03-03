# ==============================================================================
# 1. IMAGE DE BASE (Légère et sécurisée)
# ==============================================================================
FROM python:3.11-slim

# On définit le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# ==============================================================================
# 2. INSTALLATION DU MOTEUR (uv)
# ==============================================================================
# Astuce avancée : On récupère l'exécutable uv directement depuis son image officielle
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# ==============================================================================
# 3. GESTION DES DÉPENDANCES (Optimisation du cache Docker)
# ==============================================================================
# On copie uniquement les fichiers de configuration en premier
COPY pyproject.toml uv.lock ./

# On installe UNIQUEMENT les dépendances de production (--no-dev)
# --frozen garantit qu'on utilise exactement les versions du uv.lock
RUN uv sync --no-dev --frozen

# ==============================================================================
# 4. CODE SOURCE ET EXÉCUTION
# ==============================================================================
# On copie notre logique métier et notre fichier CSV
COPY app/ ./app/

# On définit la commande par défaut au démarrage du conteneur
CMD ["uv", "run", "--no-dev", "python", "app/main.py"]