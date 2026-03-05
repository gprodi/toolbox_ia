# 1. Même base OS légère
FROM python:3.12-slim

# 2. Installation de notre gestionnaire de paquets ultra-rapide
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 3. Dossier de travail
WORKDIR /app

# 4. Gestion du cache pour les dépendances du Front
COPY pyproject.toml .
RUN uv sync

# 5. Copie du code source (main.py du front)
COPY . .

# 6. Commande de démarrage Streamlit
# --server.address=0.0.0.0 est vital dans Docker pour autoriser les connexions entrantes
# --server.port=8501 est le port par défaut de Streamlit
CMD ["uv", "run", "streamlit", "run", "main.py", "--server.address=0.0.0.0", "--server.port=8501"]