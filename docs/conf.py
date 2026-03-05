# Configuration file for the Sphinx documentation builder.

import os
import sys

# CORRECTION MÉTIER : On permet à Sphinx de scanner l'API ET le Front
# C'est indispensable pour que l'autodoc trouve tes modules.
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

# On ignore les dossiers de build pour ne pas polluer la génération
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
language = "fr"

# -- Options for HTML output -------------------------------------------------
html_theme = "furo"
html_title = "Toolbox IA - Documentation Officielle"
html_logo = "docs/_static/img/logo.png"

# Les fichiers statiques (comme le logo ou le badge coverage généré)
html_static_path = ["_static"]