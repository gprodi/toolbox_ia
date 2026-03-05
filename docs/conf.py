import os
import sys

# L'UNIQUE CHEMIN NÉCESSAIRE : On se place directement dans le dossier API.
# Ainsi Python trouve "main", "models" et "modules" naturellement lors de l'importation.
sys.path.insert(0, os.path.abspath("../app_api"))

project = "toolbox_IA"
copyright = "2026, Prodi.G"
author = "Prodi.G"
release = "2.0.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "myst_parser",
    "sphinxcontrib.redoc", # Nouvelle extension ajoutée
]

# On ne mocke que le front. SQLAlchemy et les BDD fonctionnent très bien
# puisque tes tests "test_api.py" passent avec succès dans le pipeline !
autodoc_mock_imports = ["streamlit", "requests"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
language = "fr"

html_theme = "furo"
html_title = "Toolbox IA - Documentation Officielle"
html_static_path = ["_static"]

# --- Configuration de ReDoc ---
redoc = [
    {
        "name": "API Toolbox IA",
        # Le nom du fichier HTML qui sera généré dynamiquement par l'extension
        "page": "api_reference", 
        # Le chemin vers le fichier extrait à l'Étape 1
        "spec": "openapi.json",  
        "embed": True,
    }
]