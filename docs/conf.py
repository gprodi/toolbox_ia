# Configuration file for the Sphinx documentation builder.

import os
import sys

# 1. On ajoute LA RACINE du projet pour différencier app_api.main et app_front.main
sys.path.insert(0, os.path.abspath(".."))
# 2. On garde app_api pour que l'API trouve ses propres dépendances internes (models, etc.)
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
]

# Leurre pour ignorer l'absence de Streamlit lors de la génération de la doc
autodoc_mock_imports = ["streamlit", "requests"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
language = "fr"

html_theme = "furo"
html_title = "Toolbox IA - Documentation Officielle"
html_static_path = ["_static"]
html_logo = "_static/img/logo.png"  # Assure-toi d'avoir ce logo dans le dossier _static
