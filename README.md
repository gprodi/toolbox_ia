# 🧮 Toolbox IA - V2 (Micro-services)

Bienvenue dans la Toolbox IA V2 ! Ce projet est passé d'un simple script Python à une véritable architecture modulaire, robuste et conteneurisée.

![CI Status](https://github.com/gprodi/toolbox_ia/actions/workflows/ci.yml/badge.svg)
![Coverage](https://gprodi.github.io/toolbox_ia/coverage.svg)
![Python Version](https://img.shields.io/badge/Python-3.12-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🏗️ Architecture du Projet

L'application est découpée en micro-services isolés :

* **API (FastAPI)** : Le "Cerveau". Gère la logique métier (mon_module.py), les contrats de données (Pydantic) et la communication avec la base de données.

* **Frontend (Streamlit)** : L'interface utilisateur. Isolée et réactive.

* **Database (PostgreSQL)** : Assure la persistance des opérations mathématiques.

## 🚀 Guide d'Installation

C'est la méthode de production. Vous n'avez besoin que de Docker et de Docker Compose.

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/gprodi/toolbox_ia.git
   cd toolbox_ia
   ```

2. **Préparez vos secrets en copiant le template :**

    ```bash
    cp .env.example .env
    ```

3. **Lancez l'infrastructure complète :**

   ```bash
    export DOCKERHUB_USERNAME="votre_pseudo_dockerhub"
    docker-compose -f docker-compose.prod.yml up -d
   ```

4. **Accédez aux services :**

    * Frontend : <http://localhost:8501>

    * Documentation API (Swagger) : <http://localhost:8000/docs>

## 💻 Développement Local (Docker)

Si vous développez sur le code, l'application utilise l'outil uv pour une gestion ultra-rapide des environnements virtuels.

1. **Si vous souhaitez modifier le code et tester l'architecture complète sur votre machine avec un rechargement des conteneurs : :**

   ```bash
    docker-compose up --build

   ```

(Note : N'oubliez pas d'éteindre l'environnement de production avec docker-compose -f docker-compose.prod.yml down avant de lancer le développement pour éviter les conflits de ports).

## 💻 Développement Local (via uv)

Si vous développez sur le code, l'application utilise l'outil uv pour une gestion ultra-rapide des environnements virtuels.

1. **Lancer l'API :**

   ```bash
    cd app_api
    uv sync
    uv run fastapi dev main.py

   ```

2. **Lancer le Front (dans un autre terminal) :**

    ```bash
    cd app_front
    uv sync
    uv run streamlit run main.py
    ```

## 📚 Documentation & Tests

La documentation technique (Sphinx/Furo) est générée automatiquement dans les GitHub Pages. Les tests d'API sont assurés par Pytest.

1. **Lancer les tests unitaires:**

   ```bash
    cd app_api
    uv run pytest ../tests/test_api.py

   ```

## 🤝 Contribuer

Consultez notre [page de gouvernance dédiée](governance.rst).

## 👥 Contributeurs

* **Prodi.G** - *Ingénieur / Créateur*

## 📄 Licence

Ce projet est sous licence MIT.
Consultez la [page de licence](license.rst).
