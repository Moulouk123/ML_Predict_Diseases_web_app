# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model=pickle.load(open('C:/Users/Moulouk/Desktop/Stage_ML/diabetes_model.sav','rb'))
heart_disease_model=pickle.load(open('C:/Users/Moulouk/Desktop/Stage_ML/heart_disease_model.sav','rb'))
breast_cancer_model=pickle.load(open('C:/Users/Moulouk/Desktop/Stage_ML/Breast_Cancer_model.sav','rb'))
parkinsons_model=pickle.load(open('C:/Users/Moulouk/Desktop/Stage_ML/Parkinson_Disease_model.sav','rb'))

#sidebar for navigate
with st.sidebar:
    selected=option_menu('multiple Disease Prediction System', ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction','Breast Cancer Prediction'],icons=['activity','heart','person' ,'gender-female'],default_index=0 )

#Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    # getting the input data from the user
    col1, col2,col3= st.columns(3)
    with col1:
        Age = st.text_input('Age')
    with col2:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col3:
        Glucose = st.text_input('Glucose Level')

    with col1:
        BMI = st.text_input('BMI value')

    with col2:
        Insuline = st.text_input('Insuline')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose,  BMI,Age,Insuline]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
            st.warning(diab_diagnosis)
        else:
            diab_diagnosis = 'The person is not diabetic'
            st.success(diab_diagnosis)
            

    
    
if (selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        sex = st.text_input('Sex')
    with col2:
        cp = st.text_input('Chest Pain types ("cp")')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl ("fbs")')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results ("restecg")')

 

    with col2:
        exang = st.text_input('Exercise Induced Angina ("exang")')

    with col3:
        oldpeak = st.text_input('ST depression induced by exercise ("oldpeak")')

    with col1:
        slope = st.text_input('Slope of the peak exercise ST segment ("slope")')

    with col2:
        ca = st.text_input('Major vessels colored by flourosopy ("ca")')

    with col3:
        thal = st.text_input('thal ("thal")')


    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [sex, cp,fbs, restecg, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
            st.warning(heart_diagnosis)
        else:
            heart_diagnosis = 'The person does not have any heart disease'
            st.success(heart_diagnosis)
    
if (selected == 'Parkinsons Prediction'):
    st.title('Parkinsons  Prediction using ML')
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col2:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col3:
        RAP = st.text_input('MDVP:RAP')

    with col4:
        DDP = st.text_input('Jitter:DDP')

    with col5:
        APQ = st.text_input('MDVP:APQ')
    with col1:
        RPDE = st.text_input('RPDE')
    with col2:
        DFA = st.text_input('DFA')
    with col3:
        spread1 = st.text_input('spread1')
    with col4:
        spread2 = st.text_input('spread2')     
    with col5:
        PPE = st.text_input('PPE')
  
    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [ Jitter_percent, Jitter_Abs,RAP, DDP,APQ,  RPDE, DFA, spread1, spread2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
            st.warning(diab_diagnosis)
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
            st.success(parkinsons_diagnosis)
    

if selected == 'Breast Cancer Prediction':
    st.title('Breast Cancer Prediction using ML')

    # Create columns for user input
    col1, col2 ,col3= st.columns(3)

    with col1:
        mean_radius = st.text_input('mean radius', key='mean_radius')
        mean_compactness = st.text_input('mean compactness', key='mean_compactness')
        mean_concavity = st.text_input('mean concavity', key='mean_concavity')
      

    with col2:
        worst_smoothness = st.text_input('worst smoothness', key='worst_smoothness')
        worst_compactness = st.text_input('worst compactness', key='worst_compactness')
        worst_concavity = st.text_input('worst concavity', key='worst_concavity')

        
    with col3:
        texture_error = st.text_input('texture error', key='texture_error')
        worst_radius = st.text_input('worst radius', key='worst_radius')
        worst_concave_points = st.text_input('worst concave points', key='worst_concave_points')
        worst_symmetry = st.text_input('worst symmetry', key='worst_symmetry')
        
    # Create a button for Prediction
    if st.button("Breast Cancer Prediction"):
        # Collect all user inputs
        user_input = [
            mean_radius, mean_compactness, mean_concavity, texture_error,
            worst_radius, worst_smoothness, worst_compactness,
            worst_concavity, worst_concave_points, worst_symmetry
        ]


        # Convert input to float
        user_input = [float(x) for x in user_input]

        # Make prediction
        breast_cancer_prediction = breast_cancer_model.predict([user_input])

        # Display the prediction
        if breast_cancer_prediction[0] == 0:
            st.warning("The Breast Cancer is Malignant")
        else:
            st.success("The Breast Cancer is Benign")



   
