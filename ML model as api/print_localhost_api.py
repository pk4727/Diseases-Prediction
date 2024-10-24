# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 16:50:17 2023

@author: Pradhuman_kumar(pk)
"""

import json 
import requests

url = 'https://f3e8-35-245-171-156.ngrok.io/diabetes_prediction'

input_data = {
    'Pregnancy' : 1,
    'Glucose' :  85,
    'BloodPressure' : 66,
    'SkinThikness' : 29,
    'Insulin' : 0,
    'BMI' : 26.6,
    'DiabetesPedigreeFunction' : 0.351,
    'Age' : 31
    }

input_json = json.dumps(input_data)
response = requests.post(url, data=input_json)
print(response.text)