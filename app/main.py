import sys
from pathlib import Path  # On ajoute cet import

from loguru import logger
from modules.mon_module import add, print_data, square


def setup_logging():
    """Configure Loguru pour créer un fichier unique par exécution."""
    # 1. Définition du dossier de base (racine du projet)
    base_dir = Path(__file__).resolve().parent.parent
    log_dir = base_dir / "logs"
    log_dir.mkdir(exist_ok=True)

    # 2. Nettoyage de la configuration existante
    logger.remove()

    # 3. Ajout de la console (Niveau INFO pour ne pas polluer l'écran)
    logger.add(
        sys.stderr,
        level="INFO",
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>",  # noqa: E501
    )

    # 4. Ajout du fichier de log DATÉ (Niveau DEBUG pour tout capturer)
    # La balise {time} est automatiquement remplacée par Loguru
    log_path = log_dir / "toolbox_{time:YYYY-MM-DD_HH-mm-ss}.log"

    logger.add(
        str(log_path),
        rotation="10 MB",
        retention="10 days",
        level="DEBUG",
        encoding="utf-8",
    )

    logger.info("🚀 Nouvelle session de logging initialisée.")


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
    from pathlib import Path  # NOUVEAU : Déjà importé en haut, mais on s'en sert ici

    import pandas as pd

    try:
        # NOUVEAU : On calcule le chemin absolu du dossier contenant main.py
        current_dir = Path(__file__).resolve().parent
        # On y accole le nom du fichier. Ainsi, la commande marchera d'où qu'on la lance
        csv_path = current_dir / "moncsv.csv"

        df = pd.read_csv(csv_path)
        print_data(df)
    except FileNotFoundError:
        # NOUVEAU : On utilise le chemin calculé dans le log pour faciliter le débogage
        logger.error(f"Fichier de données introuvable au chemin : {csv_path}")


if __name__ == "__main__":
    main()
