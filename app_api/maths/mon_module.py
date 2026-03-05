import pandas as pd
import pandera.pandas as pa  # NOUVEAU : Importation du validateur
from loguru import logger


def add(a: int | float, b: int | float) -> int | float:
    """Additionne deux nombres.

    Args:
        a (int | float): Le premier nombre.
        b (int | float): Le deuxième nombre.

    Returns:
        int | float: La somme de a et b.

    """
    return a + b


def sub(a: int | float, b: int | float) -> int | float:
    """Soustrait le second nombre du premier.

    Args:
        a (int | float): Le nombre de base.
        b (int | float): Le nombre à soustraire.

    Returns:
        int | float: La différence entre a et b.

    """
    return a - b


def square(a: int | float) -> int | float:
    """Calcule le carré d'un nombre.

    Args:
        a (int | float): Le nombre à élever au carré.

    Returns:
        int | float: Le carré de a.

    """  # noqa: D401
    return a * a


# NOUVEAU : Définition du schéma attendu. C'est notre contrat de confiance.
# On exige une colonne 'id' (entière) et une colonne 'valeur' (entière).
CSVDataFrameSchema = pa.DataFrameSchema(
    {"id": pa.Column(int, required=True), "valeur": pa.Column(int, required=True)}
)


# NOUVEAU : Le décorateur valide automatiquement le 'df' en entrée avant l'exécution.
@pa.check_input(CSVDataFrameSchema)
def print_data(df: pd.DataFrame) -> int:
    """Affiche un DataFrame Pandas et retourne son nombre de lignes."""
    if df.empty:
        logger.warning("Tentative d'affichage d'un DataFrame vide.")
        return 0  # FIX : Retourner 0 plutôt que None (pour respecter le type de retour int)  # noqa: E501

    logger.info(f"Affichage de {len(df)} lignes de données.")
    print(df)
    print("=== Aperçu des données ===")
    print(df.head())
    print("==========================")
    return len(df)
