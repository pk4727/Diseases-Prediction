# upload the .sav model file

# !pip install fastapi
# !pip install uvicorn
# !pip install pickle5
# !pip install pydantic
# !pip install scikit-learn
# !pip install requests
# !pip install pypi-json
# !pip install pyngrok
# !pip install nest-asyncio

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import uvicorn
from pyngrok import ngrok
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio

app = FastAPI()

origins = ["*"]                 # it allow all domain to access
app.add_middleware(
    CORSMiddleware,             # Cross-origin resource sharing (CORS) 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class model_input(BaseModel):

    Pregnancy : int
    Glucose : int
    BloodPressure : int
    SkinThikness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int


    # loading the saved model
diabetes_model = pickle.load(open('D:\\code\\python\\ML\\ML_project\\for website_apps_streamlit\\ML model as api\\for_public_global_api.py', 'rb'))


@app.post('/diabetes_prediction')
def diabetes_predd(input_parameters : model_input):

    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    preg = input_dictionary['Pregnancy']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThikness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']


    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]

    prediction = diabetes_model.predict([input_list])

    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'


# for public url for local host and public url use in google colab
ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)