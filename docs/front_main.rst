Interface Utilisateur (Streamlit)
=================================

L'interface utilisateur de la Toolbox IA est construite avec **Streamlit**.

Contrairement à l'API qui est une bibliothèque de fonctions, le Frontend est un script exécuté de haut en bas. Il gère :

1. **La récolte des entrées** : Intercepte le type d'opération et les valeurs numériques saisies par l'utilisateur.
2. **Le routage** : Construit le payload JSON.
3. **La communication HTTP** : Envoie les données (via ``requests``) au micro-service API.
4. **L'affichage dynamique** : Restitue les résultats ou les erreurs API de manière conviviale.

*Note architecturale : Ce module respecte le principe de responsabilité unique. Il ne contient aucune logique mathématique complexe ni aucun accès direct à la base de données.*