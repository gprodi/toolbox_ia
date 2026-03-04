# 🧰 Toolbox IA : Fondations & Excellence Technique

![CI Status](https://github.com/gprodi/toolbox_ia/actions/workflows/ci.yml/badge.svg)
![Coverage](https://gprodi.github.io/toolbox_ia/coverage.svg)
![Python Version](https://img.shields.io/badge/Python-3.11%20|%203.12%20|%203.13-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Bienvenue dans la Toolbox IA de référence. Ce projet démontre la mise en place d'un environnement de développement professionnel, automatisé et documenté pour les travaux en Intelligence Artificielle.

## ✨ Fonctionnalités

* **Architecture Modulaire** : Séparation stricte de la logique métier et de l'orchestration, avec chemins relatifs robustes via `Pathlib`.
* **Validation Stricte (Data Contracts)** : Typage et validation rigoureuse des DataFrames grâce à `Pandera`.
* **Excellence Technique** : Linting intraitable avec `Ruff` (incluant les règles avancées Bugbear et PyUpgrade) et couverture de test à 100% avec `Pytest`.
* **Observabilité** : Logging structuré, coloré et rotatif via `Loguru`.
* **Intégration Continue Multi-Environnements** : Pipeline GitHub Actions testant automatiquement le code sur Python 3.11, 3.12 et 3.13.
* **Documentation Automatisée** : Site web généré via `Sphinx` et le thème `Furo`, dans un job CI/CD isolé.
* **Déploiement Sécurisé** : Conteneurisation `Docker` optimisée et sécurisée (exécution *Rootless* via un utilisateur non-privilégié).

## 🚀 Guide d'Installation

Ce projet utilise [uv](https://github.com/astral-sh/uv) pour une gestion ultra-rapide et déterministe des dépendances.

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/gprodi/toolbox_ia.git
   cd toolbox_ia
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
    docker run --rm -v ${PWD}/logs:/app/logs toolbox_ia
```

## 🤝 Contribuer

Consultez notre [page de gouvernance dédiée](governance.rst).

## 👥 Contributeurs

* **Prodi.G** - *Ingénieur / Créateur*

## 📄 Licence

Ce projet est sous licence MIT.
Consultez la [page de licence](license.rst).
