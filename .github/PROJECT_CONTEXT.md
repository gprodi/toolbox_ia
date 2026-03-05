# Mémo : Projet 2 - Orchestration & Micro-services

## 1. L'Arborescence du Projet

L'application est divisée en micro-services isolés :

* app_front/ : Gère l'interface (Streamlit). Communique uniquement avec l'API.

* app_api/ : Gère la logique métier (FastAPI) et l'accès aux données.

* Base de données : Gérée via l'image officielle PostgreSQL dans Docker.

## 2. Concepts Clés Appris

* Micro-services : Découpage d'une application en petits services indépendants, facilitant la maintenance et la scalabilité.

* API REST (FastAPI) : Interface de programmation permettant au Front et au Backend de communiquer de manière standardisée via le protocole HTTP.

* Contrats de Données (Pydantic) : Validation stricte des données entrantes et sortantes pour éviter les crashs et les failles d'injection.

* Orchestration (Docker Compose) : Outil permettant de lancer et de faire communiquer plusieurs conteneurs Docker (Front, API, BDD) avec une seule commande.

* Docker Volumes : Mécanisme permettant de persister les données de la base de données même si le conteneur est détruit.

* Réseaux Docker (Networks) : Isolation réseau. Le Front est sur un réseau front-api, la BDD sur un réseau api-db. Le Front ne peut pas voir la BDD.

* Gitleaks : Outil de sécurité intégré à la CI pour s'assurer qu'aucun mot de passe ou clé d'API n'est poussé sur GitHub.

## 3. Commandes Terminal Essentielles

* uv sync : Synchroniser les dépendances d'un sous-projet.

* uv run fastapi dev app_api/main.py : Lancer l'API en mode développement (rechargement à chaud).

* uv run streamlit run app_front/main.py : Lancer l'interface utilisateur.

* uv run pytest : Lancer la suite de tests unitaires.

* docker-compose up --build : Construire et lancer toute l'infrastructure micro-services en local.

* docker-compose down -v : Éteindre l'infrastructure et détruire les volumes (remise à zéro).
