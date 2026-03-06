"""
Point d'entrée principal de l'API Toolbox IA.

Ce module définit l'application FastAPI et ses routes (endpoints) RESTful.
Il sert d'interface entre le monde extérieur (requêtes HTTP) et la logique
métier interne de l'application (opérations mathématiques et base de données).

L'application est automatiquement documentée par FastAPI via Swagger UI
(disponible sur /docs).
"""

import logging

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from models.models import OperationCreate, OperationResponse
from modules import crud
from modules.connect import Base, engine, get_db

logger = logging.getLogger(__name__)

# Création des tables BDD
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Toolbox IA - Core API",
    description="API Micro-service pour la gestion des mathématiques et données.",
    version="2.0.0",
)


# NOUVEAU : La fameuse route racine (Healthcheck) que le test cherchait !
@app.get("/", tags=["Healthcheck"])
def read_root():
    """
    Vérifie l'état de santé de l'API.
    Retourne un simple message de statut.
    """
    return {"status": "En ligne", "message": "Bienvenue sur l'API Toolbox 2.0 !"}


@app.post(
    "/operations/",
    response_model=OperationResponse,
    status_code=status.HTTP_201_CREATED,
)
def creer_une_operation(op: OperationCreate, db: Session = Depends(get_db)):
    """
    Crée, calcule et enregistre une nouvelle opération mathématique
    en base de données.

    Ce endpoint reçoit une charge utile (payload) JSON validée par le schéma
    `OperationCreate`.
    Il délègue l'exécution mathématique et l'insertion en base de données
    au module `crud`.

    Args:
        op (OperationCreate): L'objet contenant les paramètres de l'opération
        (valeur1, valeur2, type_op).
        db (Session, optional): La session SQLAlchemy injectée par dépendance.

    Returns:
        OperationResponse: Un dictionnaire sérialisé contenant toutes
        les informations de l'opération.

    Raises:
        HTTPException:
            - **Code 400 (Bad Request)** : Si le type d'opération
            demandé n'est pas supporté.
            - **Code 500 (Internal Server Error)** : Si une erreur
            inattendue survient.
    """
    logger.info(f"Requête reçue pour une opération de type : {op.type_op}")

    try:
        nouvelle_op = crud.create_operation(db=db, op=op)
        logger.info(f"Opération sauvegardée en BDD avec l'ID: {nouvelle_op.id}")
        return nouvelle_op

    except ValueError as ve:
        logger.warning(f"Erreur de validation métier : {ve}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ve))

    except Exception as e:
        logger.error(f"Erreur interne inattendue : {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Une erreur interne est survenue.",
        )
