
import pickle

with open('modele.pkl', 'rb') as fichier:
    modele_charge = pickle.load(fichier)

def prediction(modele_charge, data):
    predictions = modele_charge.predict(data)
    return predictions

