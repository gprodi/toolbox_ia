import os

import requests
import streamlit as st

# Configuration de l'URL de l'API via variable d'environnement
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.set_page_config(page_title="Toolbox IA - Micro-services", page_icon="🚀")

st.title("🧮 Toolbox IA - V2")
st.markdown("Cette interface discute en direct avec notre micro-service FastAPI isolé.")

# CORRECTION UX : Le sélecteur est sorti du formulaire.
# Ainsi, chaque changement d'opération force Streamlit à relire la page instantanément.
st.subheader("Choix de l'opération")
type_op = st.selectbox("Opération", ["add", "sub", "square"])

# Création du formulaire (uniquement pour les valeurs à envoyer)
with st.form("operation_form"):
    st.subheader("Valeurs")

    # On n'a plus besoin que de 2 colonnes maintenant
    col1, col2 = st.columns(2)

    with col1:
        val1 = st.number_input("Valeur 1", value=0.0)

    with col2:
        # La condition marche en temps réel car le formulaire est reconstruit
        # avec la nouvelle valeur de `type_op` choisie juste au-dessus !
        val2 = st.number_input("Valeur 2", value=0.0, disabled=(type_op == "square"))

    submitted = st.form_submit_button("Calculer via l'API")

# Traitement de la requête HTTP
if submitted:
    payload = {"type_op": type_op, "valeur1": val1, "valeur2": val2}

    try:
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
            "🚨 Impossible de joindre l'API. As-tu bien lancé l'API dans un autre terminal ?"
        )  # noqa: E501
