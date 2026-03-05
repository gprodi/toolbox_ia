import os
import sys

# CORRECTION MÉTIER : On pointe vers app_api pour trouver les modules
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
    "myst_parser",  # Pour lire le README.md
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "fr"

html_theme = "furo" # Ton thème favori
html_title = "Toolbox IA - Documentation Officielle"
html_static_path = ["_static"]