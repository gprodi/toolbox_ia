"""
Point d'entrée principal de l'API Toolbox IA.

Ce module définit l'application FastAPI et ses routes (endpoints) RESTful.
Il sert d'interface entre le monde extérieur (requêtes HTTP) et la logique
métier interne de l'application (opérations mathématiques et base de données).

L'application est automatiquement documentée par FastAPI via Swagger UI (disponible sur /docs).
"""

import logging

from fastapi import Depends, FastAPI, HTTPException, status
from models.models import OperationCreate, OperationDB, OperationResponse
from modules import crud  # On importe notre archiviste
from modules.connect import Base, engine, get_db
from sqlalchemy.orm import Session

# Configuration des logs
logger = logging.getLogger(__name__)

# Création magique des tables dans la base de données au lancement !
# (Dans un vrai projet de grande ampleur, on utiliserait un outil comme Alembic pour ça)
Base.metadata.create_all(bind=engine)

# Initialisation de l'application FastAPI
app = FastAPI(
    title="Toolbox IA - Core API",
    description="API Micro-service pour la gestion des mathématiques et des données.",
    version="2.0.0",
)


@app.post(
    "/operations/",
    response_model=OperationResponse,
    status_code=status.HTTP_201_CREATED,
)
def creer_une_operation(op: OperationCreate, db: Session = Depends(get_db)):
    """
    Crée, calcule et enregistre une nouvelle opération mathématique en base de données.

    Ce endpoint reçoit une charge utile (payload) JSON validée par le schéma `OperationCreate`.
    Il délègue l'exécution mathématique et l'insertion en base de données au module `crud`.

    Args:
        op (OperationCreate): L'objet contenant les paramètres de l'opération (valeur1, valeur2, type_op).
        db (Session, optional): La session SQLAlchemy injectée par dépendance pour interagir avec la BDD.

    Returns:
        OperationResponse: Un dictionnaire sérialisé contenant toutes les informations de l'opération,
        incluant l'identifiant unique généré par la BDD et le résultat du calcul.

    Raises:
        HTTPException: 
            - **Code 400 (Bad Request)** : Si le type d'opération demandé n'est pas supporté par la logique métier.
            - **Code 500 (Internal Server Error)** : Si une erreur inattendue survient lors du traitement ou de l'écriture en base.
    """
    logger.info(f"Requête reçue pour une opération de type : {op.type_op}")

    try:
        # TOUTE LA LOGIQUE EST MAINTENANT DÉLÉGUÉE AU FICHIER CRUD !
        # Le main.py se contente d'appeler la fonction et d'attendre le résultat.
        nouvelle_op = crud.create_operation(db=db, op=op)

        logger.info(f"Opération sauvegardée en BDD avec l'ID: {nouvelle_op.id}")
        return nouvelle_op

    except ValueError as ve:
        # Erreur métier (ex: type d'opération inconnu) -> Code 400 (Bad Request)
        logger.warning(f"Erreur de validation métier : {ve}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ve))

    except Exception as e:
        # Erreur imprévue (crash BDD, etc.) -> Code 500 (Internal Server Error)
        logger.error(f"Erreur interne inattendue : {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Une erreur interne est survenue lors de la création de l'opération."
        )