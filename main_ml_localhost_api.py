from fastapi import FastAPI 
from pydantic import BaseModel
import pickle
import json

app = FastAPI()
class model_input(BaseModel):
    Pregnancy : int
    Glucose :  int
    BloodPressure : int
    SkinThikness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int
    
# loading the saved model
diabetes_model = pickle.load(open('Diabetes_prediction_trained_model.sav', 'rb'))

@app.post('/diabetes_prediction')   # or get
def diabetes_pre(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dict = json.loads(input_data)
    
    Pre = input_dict['Pregnancy']
    Glu = input_dict['Glucose']
    Blo = input_dict['BloodPressure']
    Skt = input_dict['SkinThikness']
    Ins = input_dict['Insulin']
    BMI = input_dict['BMI']
    Dpf = input_dict['DiabetesPedigreeFunction']
    Age = input_dict['Age']

    input_list = [ Pre, Glu, Blo, Skt, Ins, BMI, Dpf, Age]

    prediction = diabetes_model.predict( [input_list] )

    if prediction[0] == 0:
        return ' The Person is not Diabetes.'
    else:
        return 'The Person is Diabetes.' 
    
