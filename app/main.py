import pandas as pd

# Import absolu depuis notre package local
from modules.mon_module import add, print_data, square, sub


def main() -> None:
    """Point d'entrée principal de l'application.

    Orchestre la lecture des données et l'appel aux fonctions métier.
    """
    print("Démarrage de l'application...")

    # 1. Démonstration des fonctions mathématiques
    resultat_addition = add(10, 5)
    print(f"10 + 5 = {resultat_addition}")

    resultat_carre = square(4)
    print(f"Carré de 4 = {resultat_carre}")

    # 2. Démonstration du traitement de données avec Pandas
    chemin_csv = "app/moncsv.csv"
    try:
        df = pd.read_csv(chemin_csv)
        nombre_lignes = print_data(df)
        print(f"Le fichier contient {nombre_lignes} lignes de données.")
    except FileNotFoundError:
        print(f"Erreur fatale : Le fichier {chemin_csv} est introuvable.")


# Règle d'or de l'exécution en Python
if __name__ == "__main__":
    main()
