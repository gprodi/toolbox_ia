# Guide de Contribution 🛠️

Merci de l'intérêt que vous portez à l'amélioration de la Toolbox IA ! L'excellence technique est notre priorité. Voici les règles à suivre pour que votre code soit accepté.

## Processus de Développement

1. **Ne jamais travailler sur `main`.**
2. **Créer une branche spécifique** : Utilisez la nomenclature suivante : `feat/nom-fonctionnalite` pour une nouveauté, ou `fix/nom-du-bug` pour une correction.

   ```bash
   git checkout -b feat/ajout-division

3. **Développement local** : Assurez-vous d'avoir installé les dépendances de développement (uv sync).

4. **Validation Qualité (Obligatoire)** : Avant toute soumission, votre code doit passer nos deux juges de paix :

    Linting : uv run ruff check . (aucun avertissement toléré).

    Tests : uv run pytest (la couverture doit rester à 100%).

5. **Soumettre une Pull Request (PR)** : Ouvrez une PR sur GitHub vers la branche dev ou main. Notre robot de CI exécutera automatiquement les tests. Si la CI échoue, la fusion sera bloquée.

## Philosophie du Code

Ajoutez des Docstrings au format Google pour toute nouvelle fonction.

Utilisez impérativement le Type Hinting (typage statique) de Python.

Écrivez des tests unitaires en utilisant les Fixtures et la Paramétrisation de Pytest si nécessaire.
