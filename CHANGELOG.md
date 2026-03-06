## [unreleased]

### 🚀 Features

- Affichage doc fastapi
- Réintégration de l'automatisation du changelog dans le CI
- *(ops)* Refonte complète CI/CD, séparation environnements dev/prod et ajout linter Ruff

### 🐛 Bug Fixes

- Positionnement du sys.path dans app_api pour corriger l'import Sphinx
- Instalattion sphinx redoc
- Suppression du __init__.py racine qui cassait les imports FastAPI

### 💼 Other

- *(docs)* Ajout de setuptools pour compatibilité sphinxcontrib-redoc

### 📚 Documentation

- Maj readme

### 🎨 Styling

- Correction du formatage et des imports avec ruff

### ⚙️ Miscellaneous Tasks

- *(docs)* Auto-update changelog [skip ci]
- *(docs)* Auto-update changelog [skip ci]
- *(docs)* Auto-update changelog [skip ci]
- *(docs)* Auto-update changelog [skip ci]
- *(docs)* Auto-update changelog [skip ci]
- *(docs)* Auto-update changelog [skip ci]
- *(docs)* Auto-update changelog [skip ci]
- *(docs)* Auto-update changelog [skip ci]
- *(docs)* Auto-update changelog [skip ci]
## [2.0.0] - 2026-03-05

### 🐛 Bug Fixes

- Robust docs build and path
- Include dev group in sphinx build
- Ajout des __init__.py pour transformer les dossiers en packages pour Sphinx
- Resolution finale import sphinx et nettoyage tests

### 💼 Other

- Deploiement ajouter au ci.yml

### 📚 Documentation

- Finalisation de la doc Sphinx et correction des badges
- Ajout des docstrings professionnels pour le frontend
- Utilisation des espaces de noms pour sphinx
- Finalisation de l'architecture sphinx et nettoyage des tests

### 🧪 Testing

- Ajout du healthcheck et tests exhaustifs pour coverage

### ⚙️ Miscellaneous Tasks

- Generation du changelog v2.0.0
## [1.6.0] - 2026-03-05

### 🚀 Features

- Migration V2 micro-services, dockerisation et CI/CD finalisée
- Migration V2 micro-services, dockerisation et CI/CD finalisée
## [1.5.1] - 2026-03-04

### 🐛 Bug Fixes

- *(ci)* Restauration de l'upload du badge SVG"
- *(ci)* Utilisation de noms d'artefacts dynamiques pour le badge
## [1.5.0] - 2026-03-04

### 🚀 Features

- Comtpatibilité multi versionj python
## [1.4.1] - 2026-03-03

### 🐛 Bug Fixes

- *(deps)* Abaissement de la version de sphinx pour compatibilité python 3.11
## [1.4.0] - 2026-03-03

### 🚀 Features

- *(template)* Durcissement global (pandera, pathlib, docker rootless, ci matrix)

### 📚 Documentation

- Maj README
## [1.3.0] - 2026-03-03

### 🚀 Features

- Amelioration log (un fichier log different a chaque lancement )

### 📚 Documentation

- Maj README
## [1.2.0] - 2026-03-03

### 🚀 Features

- Alignement du workflow de documentation
## [1.1.0] - 2026-03-03

### 🚀 Features

- Ajout lien cliquable dans readme
## [1.0.0] - 2026-03-03

### 🚀 Features

- Toolbox complète avec CI, Docker et Doc multi-pages
- Ajout du module de prédiction

### 🐛 Bug Fixes

- Alignement de la version Python sur 3.12 pour la CI et Docker
- Force python 3.12 and disable cache in CI
- Force python 3.12 and disable cache in CI2
- Fusion des fonctions main et ajout de la docstring

### 💼 Other

- Setup automated github pages via actions

### 📚 Documentation

- Integration de la gouvernance et de la licence dans le site Sphinx
