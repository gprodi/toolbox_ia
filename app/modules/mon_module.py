import pandas as pd


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


def print_data(df: pd.DataFrame) -> int:
    """Affiche un DataFrame Pandas et retourne son nombre de lignes.

    Args:
        df (pd.DataFrame): Le DataFrame à analyser.

    Returns:
        int: Le nombre total de lignes dans le DataFrame.

    """
    print("=== Aperçu des données ===")
    print(df.head())
    print("==========================")
    return len(df)
