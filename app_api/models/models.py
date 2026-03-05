from modules.connect import Base
from pydantic import BaseModel, Field
from sqlalchemy import Column, Float, Integer, String


# ==========================================
# 1. MODÈLE SQLALCHEMY (La Table en BDD)
# ==========================================
class OperationDB(Base):
    """Définit la structure exacte de notre table 'operations' dans SQLite/PostgreSQL."""  # noqa: E501

    __tablename__ = "operations"

    id = Column(Integer, primary_key=True, index=True)  # Clé primaire unique
    type_op = Column(String, index=True)  # ex: "addition", "soustraction"
    valeur1 = Column(Float)
    valeur2 = Column(Float)
    resultat = Column(Float)


# ==========================================
# 2. MODÈLES PYDANTIC (Le Videur de l'API)
# ==========================================
class OperationCreate(BaseModel):
    """Contrat de données pour ce que le client (Front) DOIT envoyer.Si le client envoie du texte à la place d'un float, Pydantic rejettera la requête."""  # noqa: E501

    type_op: str = Field(..., description="Le type d'opération (ex: add, sub)")
    valeur1: float = Field(..., description="La première valeur numérique")
    valeur2: float = Field(..., description="La deuxième valeur numérique")


class OperationResponse(OperationCreate):
    """Contrat de données pour ce que l'API renvoie au client.
    Hérite de OperationCreate, mais ajoute l'ID généré par la BDD et le résultat.
    """  # noqa: D205

    id: int
    resultat: float

    # Indispensable en Pydantic V2 : Permet de lire un objet SQLAlchemy (OperationDB)
    # et de le transformer en JSON automatiquement pour le Front.
    model_config = {"from_attributes": True}
