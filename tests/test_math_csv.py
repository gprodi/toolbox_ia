import pandas as pd
import pytest

# On importe les fonctions de notre module métier
# L'import suppose que le dossier racine du projet est dans le PYTHONPATH
from app.modules.mon_module import add, print_data, square, sub

# ==============================================================================
# TESTS MATHÉMATIQUES (Utilisation de la Paramétrisation)
# ==============================================================================


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (10, 2, 12),  # Cas nominal positif
        (-5, 5, 0),  # Cas avec nombre négatif
        (0, 0, 0),  # Cas limite (zéros)
        (2.5, 2.5, 5.0),  # Cas avec des flottants
    ],
)
def test_add(a, b, expected):
    """Teste la fonction d'addition avec de multiples scénarios."""
    assert add(a, b) == expected


@pytest.mark.parametrize(("a", "b", "expected"), [(10, 2, 8), (0, 5, -5), (10, 10, 0)])
def test_sub(a, b, expected):
    """Teste la fonction de soustraction."""
    assert sub(a, b) == expected


@pytest.mark.parametrize(
    ("a", "expected"),
    [
        (4, 16),
        (-4, 16),  # Le carré d'un négatif est positif
        (0, 0),
    ],
)
def test_square(a, expected):
    """Teste la fonction de mise au carré."""
    assert square(a) == expected


# ==============================================================================
# TESTS DE TRAITEMENT DE DONNÉES (Utilisation des Fixtures)
# ==============================================================================


@pytest.fixture
def dummy_dataframe():
    """Fixture Pytest générant un faux DataFrame en mémoire.

    Cela évite de lire un fichier CSV physique sur le disque.

    """
    data = {"id": [1, 2, 3], "valeur": [100, 200, 300]}
    return pd.DataFrame(data)


def test_print_data(dummy_dataframe):
    """Teste la fonction print_data.

    L'argument 'dummy_dataframe' demande à Pytest d'injecter le résultat
    de la fixture du même nom directement dans ce test.

    """
    # Exécution de la fonction avec nos fausses données
    resultat = print_data(dummy_dataframe)

    # Vérification : la fonction doit retourner le nombre de lignes (ici 3)
    assert resultat == 3


# NOUVEAU : Test du cas où le DataFrame est vide
def test_print_data_empty():
    """Vérifie le comportement de la fonction face à un DataFrame vide."""
    # On crée un DataFrame vide qui respecte notre schéma Pandera (colonnes id et valeur)  # noqa: E501
    empty_df = pd.DataFrame(columns=["id", "valeur"]).astype(int)

    # L'exécution doit déclencher le logger.warning et retourner 0
    resultat = print_data(empty_df)
    assert resultat == 0
