from fastapi.testclient import TestClient
import sys
import os

# Ajout du dossier app_api au chemin pour les imports
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../app_api"))
)

from main import app

client = TestClient(app)


def test_read_main():
    """Test du Healthcheck (la route racine '/') - Va réussir maintenant !"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "En ligne",
        "message": "Bienvenue sur l'API Toolbox 2.0 !",
    }


def test_operation_addition():
    """Test de l'addition"""
    payload = {"type_op": "add", "valeur1": 10.5, "valeur2": 5.5}
    response = client.post("/operations/", json=payload)
    assert response.status_code == 201
    assert response.json()["resultat"] == 16.0


def test_operation_soustraction():
    """NOUVEAU : Test de la soustraction pour augmenter la couverture !"""
    payload = {"type_op": "sub", "valeur1": 10.0, "valeur2": 3.0}
    response = client.post("/operations/", json=payload)
    assert response.status_code == 201
    assert response.json()["resultat"] == 7.0


def test_operation_carre():
    """NOUVEAU : Test du carré pour allumer les lignes de la fonction square !"""
    payload = {"type_op": "square", "valeur1": 4.0, "valeur2": 0.0}  # valeur2 ignorée
    response = client.post("/operations/", json=payload)
    assert response.status_code == 201
    assert response.json()["resultat"] == 16.0


def test_operation_invalide():
    """Test de la sécurité : l'API doit rejeter une opération inconnue"""
    payload = {"type_op": "operation_inconnue", "valeur1": 10, "valeur2": 5}
    response = client.post("/operations/", json=payload)
    assert response.status_code == 400
    assert "non supportée" in response.json()["detail"]
