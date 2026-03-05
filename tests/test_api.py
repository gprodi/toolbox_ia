import pytest
from fastapi.testclient import TestClient

# On importe notre application FastAPI depuis le sous-dossier app_api
import sys
import os

# Astuce : On ajoute le dossier app_api au chemin Python pour que les imports locaux marchent
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../app_api"))
)

from main import app

# Création du faux navigateur (TestClient)
client = TestClient(app)


def test_read_main():
    """Test du Healthcheck (la route racine '/')"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "En ligne",
        "message": "Bienvenue sur l'API Toolbox 2.0 !",
    }


def test_operation_addition():
    """Test de l'endpoint POST /operations/ avec une addition"""
    # 1. On prépare le payload JSON
    payload = {"type_op": "add", "valeur1": 10.5, "valeur2": 5.5}

    # 2. On simule la requête POST (comme le ferait Streamlit)
    response = client.post("/operations/", json=payload)

    # 3. On vérifie que l'API accepte (201 Created)
    assert response.status_code == 201

    # 4. On vérifie que le résultat mathématique est correct (10.5 + 5.5 = 16.0)
    data = response.json()
    assert data["resultat"] == 16.0
    assert "id" in data  # On vérifie que la BDD a bien généré un ID


def test_operation_invalide():
    """Test de la sécurité : l'API doit rejeter une opération inconnue"""
    payload = {"type_op": "operation_inconnue", "valeur1": 10, "valeur2": 5}

    response = client.post("/operations/", json=payload)

    # On vérifie que notre 'try/except' renvoie bien un 400 Bad Request
    assert response.status_code == 400
