import sys

from loguru import logger
from modules.mon_module import add, print_data, square


def setup_logging():
    """Configure Loguru pour la Toolbox."""
    logger.remove()
    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",  # noqa: E501
    )
    logger.add("logs/toolbox.log", rotation="10 MB", retention="10 days", level="DEBUG")


def main() -> None:
    """Point d'entrée principal de la Toolbox IA.

    Initialise le logging, traite les données de démonstration
    et affiche les résultats mathématiques.
    """
    setup_logging()
    logger.info("Démarrage de la Toolbox IA")

    # 1. Calculs de démonstration
    logger.debug("Exécution des calculs mathématiques...")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"Carré de 4 = {square(4)}")

    # 2. Chargement des données (Pandas)
    import pandas as pd

    try:
        df = pd.read_csv("app/moncsv.csv")
        print_data(df)
    except FileNotFoundError:
        logger.error("Fichier moncsv.csv introuvable dans app/")


if __name__ == "__main__":
    main()
