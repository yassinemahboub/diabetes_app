import streamlit as st
import numpy as np

def predict_diabetes_probability(const_coef, pregnancies_coef, glucose_coef, diastolic_coef, triceps_coef, insulin_coef, bmi_coef, dpf_coef, age_coef, pregnancies, glucose, diastolic, triceps, insulin, bmi, dpf, age):
    # Calculate linear prediction
    linear_prediction = (
        const_coef + 
        pregnancies_coef * pregnancies + 
        glucose_coef * glucose + 
        diastolic_coef * diastolic + 
        triceps_coef * triceps + 
        insulin_coef * insulin + 
        bmi_coef * bmi + 
        dpf_coef * dpf + 
        age_coef * age
    )

    # Calculate predicted probability using logistic function
    predicted_probability = 1 / (1 + np.exp(-linear_prediction))

    return predicted_probability

def main():
    st.title('Diabetes Probability Predictor')

    st.header('Enter Patient Information:')
    pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=17, step=1)
    glucose = st.number_input('Glucose Level', min_value=0, max_value=200, step=1)
    diastolic = st.number_input('Diastolic Blood Pressure', min_value=0, max_value=122, step=1)
    triceps = st.number_input('Triceps Skin Fold Thickness', min_value=0, max_value=99, step=1)
    insulin = st.number_input('Insulin Level', min_value=0, max_value=846, step=1)
    bmi = st.number_input('BMI', min_value=0.0, max_value=67.1, step=0.1)
    dpf = st.number_input('Diabetes Pedigree Function', min_value=0.078, max_value=2.42, step=0.001)
    age = st.number_input('Age', min_value=21, max_value=81, step=1)

    if st.button('Predict Probability'):
        const_coef = -9.0359
        pregnancies_coef = 0.0645
        glucose_coef = 0.0341
        diastolic_coef = -0.0139
        triceps_coef = 0.0031
        insulin_coef = -0.0018
        bmi_coef = 0.1026
        dpf_coef = 0.6945
        age_coef = 0.0371

        predicted_probability = predict_diabetes_probability(const_coef, pregnancies_coef, glucose_coef, diastolic_coef, triceps_coef, insulin_coef, bmi_coef, dpf_coef, age_coef, pregnancies, glucose, diastolic, triceps, insulin, bmi, dpf, age)
        
        st.write('Predicted probability of having diabetes:', predicted_probability.round(2))

if __name__ == '__main__':
    main()
