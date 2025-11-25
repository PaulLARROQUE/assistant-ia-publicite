import streamlit as st
import pandas as pd
from openai import OpenAI

# 🔑 Remplace "TA_CLE_API" par ta clé OpenAI
client = OpenAI(api_key="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")

st.title("Assistant IA Publicité")

# Champs utilisateur
secteur = st.text_input("Secteur de l'entreprise")
service = st.text_input("Service ou produit")
objectif = st.text_input("Objectif marketing")

# Import CSV facultatif
uploaded_file = st.file_uploader("Importer vos données CSV (facultatif)", type="csv")

if st.button("Créer la publicité"):
    # Produit le plus vendu si CSV
    produit_top = None
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        if 'produit' in data.columns and 'quantité' in data.columns:
            produit_top = data.groupby("produit")["quantité"].sum().idxmax()
    
    # Création du prompt
    prompt = f"Rédige un post publicitaire clair, engageant et amical pour un {secteur} qui propose {service} pour {objectif}."
    if produit_top:
        prompt += f" Mets en avant le produit le plus vendu : {produit_top}."
    
    # Appel API moderne OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )

    texte = response.choices[0].message.content

    # Affichage
    st.write("### Texte généré :")
    st.write(texte)

    if produit_top:
        st.write("### Recommandation simple :")
        st.write(f"Promouvoir le produit le plus vendu : {produit_top}")
