# Configuration file for the Sphinx documentation builder.

import os
import sys

# CORRECTION MÉTIER : On permet à Sphinx de scanner l'API ET le Front
sys.path.insert(0, os.path.abspath("../app_api"))
sys.path.insert(0, os.path.abspath("../app_front"))

project = "toolbox_IA"
copyright = "2026, Prodi.G"
author = "Prodi.G"
release = "2.0.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "myst_parser",
]

# 🚨 LA SOLUTION CI/CD EST ICI : Leurre pour les dépendances du Front
# Sphinx va ignorer l'absence de ces modules et générer la doc quand même !
autodoc_mock_imports = ["streamlit", "requests"]

# On ignore les dossiers de build pour ne pas polluer la génération
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
language = "fr"

# -- Options for HTML output -------------------------------------------------
html_theme = "furo"
html_title = "Toolbox IA - Documentation Officielle"
html_logo = "_static/img/logo.png"  # Assure-toi d'avoir ce logo dans le dossier _static

# Les fichiers statiques (comme ton logo)
html_static_path = ["_static"]