# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 23:29:45 2023

@author: rajme
"""

import numpy as np
import pickle
import streamlit as st



# loading the saved model
loaded_model = pickle.load(open('D:/Diabetes Prediction/diabetesPredictionModel.sav', 'rb'))


# creating a function

def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)



    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)



    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)


    if prediction[0] == 1 :
      return 'The person is Diabetic'
    else :
      return 'The person is not Diabetic'
  
    

def main():
    # title
    st.title('Diabetes Prediction Web App')
    
    
    # input data from user
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('BloodPressure value')
    SkinThickness = st.text_input('SkinThickness value')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the person')
    
    
    # prediction
    
    diagonisis = ''
    
    if st.button('Result'):
        diagonisis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    
    
    st.success(diagonisis)
    
    

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
