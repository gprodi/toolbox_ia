# Mémo : Standardisation et Excellence Technique

## Concepts Clés

Linting & Formatage : Utilisation de Ruff, un outil ultra-rapide écrit en Rust qui remplace Black, Isort et Flake8, garantissant un code lisible par tous.

Tests Non-Régression : Pytest automatise la vérification des fonctions pour s'assurer qu'une modification n'a pas cassé une fonctionnalité existante. L'utilisation de Fixtures permet de simuler des données (comme des DataFrames Pandas) sans charger de lourds fichiers externes.

CI/CD : Les GitHub Actions exécutent un robot à chaque Push ou PR pour vérifier le formatage, lancer les tests et bloquer la fusion en cas d'échec.

Conteneurisation : Le Dockerfile est le contrat garantissant que l'application tournera de manière identique partout.

## Commandes Indispensables

uv init : Initialiser le projet.

uv add `<package>` : Ajouter des bibliothèques.

uv run ruff check . : Vérification du code par la "police du code".

uv run ruff format . : Correction automatique du formatage.

uv run pytest -v --cov=app --cov-report=term-missing : Lancement du banc de test avec mesure de la couverture de code.

Stratégie d'Exécution par Jalons (Step-by-Step)
Pour garantir la qualité, nous avancerons méthodiquement. Voici notre plan :

PHASE 1 : Initialisation avec uv et configuration du pyproject.toml (Ruff & Pytest).

PHASE 2 : Développement du module métier (mon_module.py) et du point d'entrée (main.py).

PHASE 3 : Stratégie de test avancée (Paramétrisation et Fixtures pour Pandas).

PHASE 4 : Documentation Sphinx avec thème Furo et intégration du README.

PHASE 5 : Conteneurisation (Dockerfile) et Automatisation (GitHub Actions ci.yml).
