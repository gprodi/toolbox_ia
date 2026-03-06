"""
Interface Utilisateur (Frontend) de la Toolbox IA.

Ce module utilise Streamlit pour générer une interface web interactive et réactive.
Il respecte strictement l'architecture micro-services : il ne contient aucune logique
mathématique complexe ni accès direct à la base de données.

Son rôle (Responsabilité Unique) est de :
1. Récolter les entrées de l'utilisateur (type d'opération, valeurs numériques).
2. Construire un payload JSON validé implicitement par l'interface.
3. Envoyer ces données via une requête HTTP POST au micro-service API.
4. Afficher le résultat ou les erreurs retournés par l'API de manière conviviale.

Variables d'environnement requises:
    API_URL (str): L'URL complète du backend FastAPI
    (ex: http://127.0.0.1:8000 en local, ou http://api:8000 dans Docker).

Dépendances:
    - streamlit: Rendu de l'IHM.
    - requests: Client HTTP synchrone.
"""

import os

import requests
import streamlit as st

# Configuration de l'URL de l'API via variable d'environnement
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.set_page_config(page_title="Toolbox IA - Micro-services", page_icon="🚀")

st.title("🧮 Toolbox IA - V2")
st.markdown("Cette interface discute en direct avec notre micro-service FastAPI isolé.")

# Sélecteur sorti du formulaire pour une UX réactive
st.subheader("Choix de l'opération")
type_op = st.selectbox("Opération", ["add", "sub", "square"])

# Création du formulaire (uniquement pour les valeurs à envoyer)
with st.form("operation_form"):
    st.subheader("Valeurs")

    # Mise en page sur 2 colonnes
    col1, col2 = st.columns(2)

    with col1:
        val1 = st.number_input("Valeur 1", value=0.0)

    with col2:
        # La condition marche en temps réel : si "square" est choisi, champ grisé
        val2 = st.number_input("Valeur 2", value=0.0, disabled=(type_op == "square"))

    submitted = st.form_submit_button("Calculer via l'API")

# Traitement de la requête HTTP
if submitted:
    payload = {"type_op": type_op, "valeur1": val1, "valeur2": val2}

    try:
        # Appel au micro-service API
        response = requests.post(f"{API_URL}/operations/", json=payload)

        if response.status_code == 201:
            data = response.json()
            st.success(f"✅ Succès ! L'API a calculé : {data['resultat']}")
            st.info(f"💾 Sauvegardé en BDD avec l'ID : {data['id']}")
        else:
            st.error(f"❌ L'API a refusé la requête (Code {response.status_code})")
            st.json(response.json())

    except requests.exceptions.ConnectionError:
        st.error(
            "🚨 Impossible de joindre l'API. Vérifiez conteneur API est en exécution."
        )
