from fastapi import FastAPI
from pydantic import BaseModel
from model_utils import prediction, load_model
import pandas as pd

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


    # @validator('State')
    # def state_must_be_valid(cls,v):
    #     valid_states = ['IN', 'OK', 'FL', 'CT', 'NJ', 'NC', 'IL', 'RI', 'TX', 'VA', 'TN',
    #              'AR', 'MN', 'MO', 'MA', 'CA', 'SC', 'LA', 'IA', 'OH', 'KY', 'MS',
    #              'NY', 'MD', 'PA', 'OR', 'ME', 'KS', 'MI', 'AK', 'WA', 'CO', 'MT',
    #              'WY', 'UT', 'NH', 'WV', 'ID', 'AZ', 'NV', 'WI', 'NM', 'GA', 'ND',
    #              'VT', 'AL', 'NE', 'SD', 'HI', 'DE', 'DC']
    #     if v not in valid_states:
    #         raise ValueError(f"State must be on of {valid_states}")
    #     return v 
    
    # @validator('BankState')
    # def bankstate_must_be_valid(cls,v):
    #     valid_bankstate = ['OH', 'IN', 'OK', 'FL', 'DE', 'SD', 'AL', 'CT', 'GA', 'OR', 'MN',
    #             'RI', 'NC', 'TX', 'MD', 'NY', 'TN', 'SC', 'MS', 'MA', 'LA', 'IA',
    #             'VA', 'CA', 'IL', 'KY', 'PA', 'MO', 'WA', 'MI', 'UT', 'KS', 'WV',
    #             'WI', 'AZ', 'NJ', 'CO', 'ME', 'NH', 'AR', 'ND', 'MT', 'ID', 'WY',
    #             'NM', 'DC', 'NV', 'NE', 'PR', 'HI', 'VT', 'AK', 'GU', 'AN', 'EN',
    #             'VI']
    #     if v not in valid_bankstate:
    #         raise ValueError(f"Bankstate must be one of {valid_bankstate}")
    #     return v 
    
class PredictionOut(BaseModel):
    category : str
    
model = load_model()

# @app.post("/predict")
# async def predict_prod (feature_input: FeaturesInput):
#     data_input_dict = feature_input.dict()
#     data_input_df = pd.DataFrame(data_input_dict, index=[0])
#     print(data_input_df)

#     predict= prediction(model,data_input_df)
#     return PredictionOut(category=predict) 

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
    
    prediction_value = pred[0]

    return PredictionOut(category=prediction_value)

# @app.post("/predict")
# async def predict(payload: FeaturesInput):
#     features = [value for value in payload.dict().values()]


#     pred = prediction(model, [features])
#     return PredictionOut(predictions=pred)