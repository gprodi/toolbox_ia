# 🧰 Toolbox IA : Fondations & Excellence Technique

![CI Status](https://github.com/gprodi/toolbox_ia.git/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen.svg)
![Python Version](https://img.shields.io/badge/Python-3.11-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Bienvenue dans la Toolbox IA de référence. Ce projet démontre la mise en place d'un environnement de développement professionnel, automatisé et documenté pour les travaux en Intelligence Artificielle.

## ✨ Fonctionnalités

* **Architecture Modulaire** : Séparation stricte de la logique métier et de l'orchestration.
* **Excellence Technique** : Linting intraitable avec `Ruff` et couverture de test à 100% avec `Pytest`.
* **Documentation Automatisée** : Site web généré via `Sphinx` et le thème `Furo`.
* **Déploiement Universel** : Conteneurisation optimisée via `Docker`.

## 🚀 Guide d'Installation

Ce projet utilise [uv](https://github.com/astral-sh/uv) pour une gestion ultra-rapide et déterministe des dépendances.

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/TON_UTILISATEUR/TON_REPO.git
   cd TON_REPO
   ```

2. **Synchroniser l'environnement (Production) :**

    ```bash
    uv sync --no-dev
    ```

3. **Lancer l'application :**

   ```bash
   uv run python app/main.py
   ```

## 🐳 Utilisation avec Docker

Pour exécuter l'application de manière totalement isolée :

```bash
    docker build -t toolbox_ia .
    docker run --rm toolbox_ia
```

## 🤝 Contribuer

Nous encourageons vivement les contributions ! Veuillez lire notre Guide de Contribution pour comprendre notre processus de branche et de Pull Request, ainsi que notre Code de Conduite pour maintenir une communauté bienveillante.

## 👥 Contributeurs

Prodi.G - Ingénieur / Créateur

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.
