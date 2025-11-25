import streamlit as st
import pandas as pd
import openai

openai.api_key = "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"

st.title("Assistant IA Publicité")

secteur = st.text_input("Secteur de l'entreprise")
service = st.text_input("Service ou produit")
objectif = st.text_input("Objectif marketing")

uploaded_file = st.file_uploader("Importer vos données CSV (facultatif)", type="csv")

if st.button("Créer la publicité"):
    produit_top = None
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        if 'produit' in data.columns and 'quantité' in data.columns:
            produit_top = data.groupby("produit")["quantité"].sum().idxmax()
    
    prompt = f"Rédige un post publicitaire clair, engageant et amical pour un {secteur} qui propose {service} pour {objectif}."
    if produit_top:
        prompt += f" Mets en avant le produit le plus vendu : {produit_top}."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    texte = response['choices'][0]['message']['content']

    st.write("### Texte généré :")
    st.write(texte)

    if produit_top:
        st.write("### Recommandation simple :")
        st.write(f"Promouvoir le produit le plus vendu : {produit_top}")
