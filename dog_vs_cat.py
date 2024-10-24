"""
Created on Sun Jul 30 20:18:08 2023

@author: Pradhuman_kumar(pk)
"""

import numpy as np
import cv2
from tensorflow import keras
import pickle 
import streamlit as st

# loading the saved model 
saved_model = pickle.load(open("D:\code\python\ML\ML_project\image_data_processing\dog_vs_cat.sav",'rb'))

# creating a function for prediction
def diabetes_prediction(input_data):
    
    # input_image_path = 'dog_image200.jpg'                                    # input image path
    # input_image_path = 'resized_image\cat.174.jpg'                         
    input_image = cv2.imread(input_data)                               # image into numpy formate
    image_resize = cv2.resize(input_image, (224,224))                        # resizing the image shape
    image_scaled = image_resize/255                                          # scaling image in 0 to 1 range from 0 to 255
    image_reshaped = np.reshape(image_scaled, [1,224,224,3])                 # reshaping into one instance

    input_prediction = saved_model.predict(image_reshaped)                   # prediction of image in probablity
    input_pred_label = np.argmax(input_prediction)                           # prediction of image in label
    
    print(input_prediction) 
    print(input_pred_label)

    if input_pred_label == 0:
        print('The image represents a Cat')

    else:
        print('The image represents a Dog')
    # prediction of input data
    
    
# creating main function
def main():
    
    # giving a title for the web
    st.title('Diabetes_prediction App')
    image = st.input_data("image path")
    # for prediction
    dignosis = ''
    
    # create a button for prediction
    if st.button('Diabetes Test Result'):
        dignosis = diabetes_prediction(image)
    st.success(dignosis)
    
if __name__ == '__main__':
    main()