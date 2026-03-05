Point d'Entrée API (FastAPI)
============================

Ce module définit les routes (endpoints) de notre micro-service backend. 

Il agit comme le "Chef d'Orchestre" de l'API :
1. Il intercepte les requêtes HTTP du Frontend.
2. Il valide automatiquement les données grâce aux schémas Pydantic.
3. Il délègue l'exécution mathématique et la sauvegarde au module CRUD.

