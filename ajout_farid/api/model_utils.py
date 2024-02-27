
from joblib import load
import pandas as pd

def load_model(path='model.pkl'):
    model = load(path)
    return model

def prediction(model, data):
    df = pd.DataFrame(data, columns=['State', 'Zip', 'BankState', 'ApprovalFY', 'Term', 'GrAppv', 'SBA_Appv'])
    predictions = model.predict(df)
    return predictions

