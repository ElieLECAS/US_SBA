import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sklearn
import pickle


#commande : pip install streamlit (donc streamlit s'installe à l'interieur de l'environnement virtuel)
#commande : streamlit hello pour voir si tout va bien 
#commande : streamlit run nomfichier.py pour lancer dans le navigateur

# Charger le modèle à partir du fichier
with open('modele.pkl', 'rb') as fichier:
    modele_charge = pickle.load(fichier)

def prepare_inputs(State, Zip, BankState, ApprovalFY, Term, GrAppv, SBA_Appv):
    new_data = pd.DataFrame({
        'State': [State],
        'Zip': [Zip],   
        'BankState': [BankState],  
        'ApprovalFY': [ApprovalFY],
        'Term': [Term],
        'GrAppv': [GrAppv],  
        'SBA_Appv': [SBA_Appv],
    })
    return new_data

options_state = ['IN', 'OK', 'FL', 'CT', 'NJ', 'NC', 'IL', 'RI', 'TX', 'VA', 'TN',
                 'AR', 'MN', 'MO', 'MA', 'CA', 'SC', 'LA', 'IA', 'OH', 'KY', 'MS',
                 'NY', 'MD', 'PA', 'OR', 'ME', 'KS', 'MI', 'AK', 'WA', 'CO', 'MT',
                 'WY', 'UT', 'NH', 'WV', 'ID', 'AZ', 'NV', 'WI', 'NM', 'GA', 'ND',
                 'VT', 'AL', 'NE', 'SD', 'HI', 'DE', 'DC']

options_bank = ['OH', 'IN', 'OK', 'FL', 'DE', 'SD', 'AL', 'CT', 'GA', 'OR', 'MN',
                'RI', 'NC', 'TX', 'MD', 'NY', 'TN', 'SC', 'MS', 'MA', 'LA', 'IA',
                'VA', 'CA', 'IL', 'KY', 'PA', 'MO', 'WA', 'MI', 'UT', 'KS', 'WV',
                'WI', 'AZ', 'NJ', 'CO', 'ME', 'NH', 'AR', 'ND', 'MT', 'ID', 'WY',
                'NM', 'DC', 'NV', 'NE', 'PR', 'HI', 'VT', 'AK', 'GU', 'AN', 'EN',
                'VI']


    # form
with st.form(key='mon_formulaire'):
    State = st.selectbox('Sélectionnez votre État', options=options_state)
    Zip = st.number_input("Entrez votre code postal", step=1)
    BankState = st.selectbox('Sélectionnez Etat de la banque', options=options_bank)
    ApprovalFY = st.number_input("Entrez l'année de la demande de prêt", min_value=1000, max_value=9999, step=1)
    Term = st.number_input("Entrez le nombre de mensualité", step=1)
    GrAppv = st.number_input("Montant total du prêt", step=1)
    SBA_Appv = st.number_input("Montant de la garanti SBA", step=1)
    
    
    submit_button = st.form_submit_button(label='Soumettre')

    # traitement apres soumission
if submit_button:
    
    inputs = prepare_inputs(State, Zip, BankState, ApprovalFY, Term, GrAppv, SBA_Appv)
    prediction = modele_charge.predict(inputs)
    st.write(f"Prédiction : {(prediction[0])}")


