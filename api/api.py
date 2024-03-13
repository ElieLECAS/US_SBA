from fastapi import FastAPI
from pydantic import BaseModel
from model_utils import prediction, load_model

app = FastAPI()

# Modèle Pydantic pour la structure de données entrantes

class FeaturesInput(BaseModel):
    State: object
    Zip: int
    BankState: object
    ApprovalFY: int
    Term: int
    GrAppv: int
    SBA_Appv: int
   
class PredictionOut(BaseModel):
    category : str
    
model = load_model()

@app.post('/predict')
def prediction_root(feature_input:FeaturesInput):
    F1=feature_input.State
    F2=feature_input.Zip
    F3=feature_input.BankState
    F4=feature_input.ApprovalFY
    F5=feature_input.Term
    F6=feature_input.GrAppv
    F7=feature_input.SBA_Appv
    

    pred = prediction(model,[[F1,F2,F3,F4,F5,F6,F7]])
    

    return PredictionOut(category=pred)
