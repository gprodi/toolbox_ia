from sqlalchemy.orm import Session

from maths import mon_module  # On importe notre "Chef cuisinier"
from models.models import OperationCreate, OperationDB


def create_operation(db: Session, op: OperationCreate):
    """Orchestre le calcul et la sauvegarde en base de données."""
    # 1. Le Calcul (Appel au module métier)
    if op.type_op == "add":
        res = mon_module.add(op.valeur1, op.valeur2)
    elif op.type_op == "sub":
        res = mon_module.sub(op.valeur1, op.valeur2)
    elif op.type_op == "square":
        # NOUVEAU : On utilise la fonction 'square' de ton VRAI mon_module.py
        # Le carré ne prend qu'un seul paramètre, on ignore donc valeur2
        res = mon_module.square(op.valeur1)
    else:
        # On lève une erreur Python standard si l'opération est inconnue
        raise ValueError(f"Opération '{op.type_op}' non supportée.")

    # 2. La Sauvegarde en BDD
    nouvelle_op_db = OperationDB(**op.model_dump(), resultat=res)
    db.add(nouvelle_op_db)
    db.commit()
    db.refresh(nouvelle_op_db)

    return nouvelle_op_db
