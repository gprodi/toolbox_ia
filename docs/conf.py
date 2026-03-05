# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
import os
import sys

# CORRECTION MÉTIER : On indique à Sphinx où trouver notre nouveau code source (le dossier app_api)
# Le radar pointe désormais vers l'API, qui contient notre logique métier (maths).
sys.path.insert(0, os.path.abspath("../app_api"))

project = "toolbox_IA"
copyright = "2026, Prodi.G"
author = "Prodi.G"
release = "1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Aspire les docstrings du code
    "sphinx.ext.mathjax",  # Pour latex
    "sphinx.ext.viewcode",  # pour afficher code source
    "sphinx.ext.napoleon",  # Traduit le format Google en format Sphinx
    "myst_parser",  # Permet d'inclure des fichiers Markdown (comme le README)
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "fr"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = (
    "furo"  # Utilisation du thème Furo (assurez-vous de l'avoir installé avec uv)
)
html_logo = "_static/img/logo.png"
html_static_path = ["_static"]
