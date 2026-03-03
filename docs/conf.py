# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
import os
import sys

# On indique à Sphinx où trouver notre code source (le dossier app)
sys.path.insert(0, os.path.abspath("../app"))

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

html_theme = "furo"
html_logo = "_static/img/logo.png"
html_static_path = ["_static"]
html_title = "Toolbox IA - Documentation Officielle"
