"""
Created on Sun Jul 30 20:18:08 2023

@author: Pradhuman_kumar(pk)
"""

import numpy as np
import pickle 
import streamlit as st

# loading the saved model 
load_model = pickle.load(open("D:\\code\\python\\ML\\ML_project\\for website_apps_streamlit\\Diabetes_prediction_trained_model.sav",'rb'))

# creating a function for prediction
def diabetes_prediction(input_data):
    
    # input to numpy value and reshape it to one instance
    indata_numpy=np.asarray(input_data) 
    idata=indata_numpy.reshape(1,-1) 
    
    # prediction of input data
    ANS=load_model.predict(idata)
    if ANS==0:
        return ' Person have NOT Diabetes.'
    elif ANS==1:
        return ' Person have Diabetes.'
    
# creating main function
def main():
    
    # giving a title for the web
    st.title('Diabetes_prediction App')
    
    # getting the input data by user
    # Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    Pregnancies = st.text_input('Number Of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('Number of BMI Value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction Value')
    Age = st.text_input('Age Of The Person')
    
    # for prediction
    dignosis = ''
    
    # create a button for prediction
    if st.button('Diabetes Test Result'):
        dignosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    st.success(dignosis)
    
if __name__ == '__main__':
    main()