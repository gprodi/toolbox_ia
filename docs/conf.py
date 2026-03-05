import os
import sys

# La Règle d'Or : On pointe UNIQUEMENT vers le cerveau (API)
# L'API contient de la vraie logique métier (fonctions, classes) à aspirer.
sys.path.insert(0, os.path.abspath(".."))

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

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
language = "fr"

html_theme = "furo"
html_title = "Toolbox IA - Documentation Officielle"
html_static_path = ["_static"]
html_logo = "_static/img/logo.png"  # Assure-toi d'avoir ce logo dans le dossier _static
