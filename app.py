import streamlit as st
import pandas as pd
from transformers import pipeline

# Générateur de texte léger pour test
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")



st.title("Assistant IA Publicité Simplifié")

secteur = st.text_input("Secteur de l'entreprise")
service = st.text_input("Service ou produit")
objectif = st.text_input("Objectif marketing")

uploaded_file = st.file_uploader("Importer vos données CSV (facultatif)", type="csv")

if st.button("Créer la publicité"):

prompt = f"Rédige un post publicitaire accrocheur et amical pour un {secteur} qui propose {service} pour {objectif}."

    """
    
    texte = generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']

    
    st.write("### Texte généré :")
    st.write(texte)

    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        if 'produit' in data.columns and 'quantité' in data.columns:
            produit_top = data.groupby("produit")["quantité"].sum().idxmax()
            st.write("### Recommandation simple :")
            st.write(f"Promouvoir le produit le plus vendu : {produit_top}")
        else:
            st.write("Les colonnes 'produit' et 'quantité' sont nécessaires pour les recommandations.")
