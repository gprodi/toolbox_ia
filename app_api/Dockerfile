# 1. L'OS de base : On part d'un Linux ultra-léger (slim) avec Python 3.12 pré-installé
FROM python:3.12-slim

# 2. Astuce DevOps : On récupère l'outil "uv" directement depuis son image officielle
# C'est la méthode la plus propre et rapide pour l'installer dans notre conteneur
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 3. On définit notre dossier de travail à l'intérieur du conteneur
WORKDIR /app

# 4. On copie D'ABORD le pyproject ET le fichier lock pour garantir un build déterministe
COPY pyproject.toml uv.lock ./

# 5. On installe UNIQUEMENT les dépendances de production, en mode figé (--frozen)
RUN uv sync --no-dev --frozen

# 6. Maintenant, on copie le reste de notre code (main.py, models/, modules/...)
COPY . .

# 7. La commande pour démarrer le moteur ! 
# On utilise "fastapi run" (au lieu de "dev") car c'est la commande de production.
# IMPORTANT : host "0.0.0.0" permet à l'API d'être joignable de l'extérieur du conteneur.
CMD ["uv", "run", "fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8000"]