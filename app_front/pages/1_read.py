import os

import pandas as pd
import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.title("📖 Historique des Opérations")
st.markdown("Voici toutes les opérations sauvegardées dans notre base PostgreSQL.")

if st.button("Rafraîchir les données"):
    try:
        # On demande poliment l'historique à l'API
        response = requests.get(f"{API_URL}/operations/")

        if response.status_code == 200:
            data = response.json()

            if len(data) == 0:
                st.info("Aucune opération n'a encore été enregistrée.")
            else:
                # Magie de Streamlit : on transforme le JSON en DataFrame Pandas
                # pour un bel affichage
                df = pd.DataFrame(data)
                # On peut réorganiser ou renommer les colonnes si on le souhaite
                st.dataframe(df, use_container_width=True)

        else:
            st.error(f"Erreur de l'API : {response.status_code}")

    except requests.exceptions.ConnectionError:
        st.error("🚨 Impossible de joindre l'API.")
