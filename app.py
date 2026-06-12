import streamlit as st
import joblib
import pandas as pd
import time

@st.cache_resource
def load_model():
    return joblib.load('full_pipeline.pkl')

pipeline = load_model()

st.title('آیا مشتری شما خواهد رفت یا خیر')
st.text('این برنامه پیش‌بینی می‌کند که مشتری بانک را ترک می‌کند یا خیر')
st.image('https://slitayem.github.io/img/blog/2020-08-04/churn.png')

def input_user():
    credScore = st.slider('Credit Score', 350, 850, 500)
    age = st.slider('Age', 18, 100, 30)
    balance = st.slider('Balance', 0, 260000, 100000)
    num_products = st.slider('Number of Products', 1, 4, 2)
    estimated_salary = st.slider('Estimated Salary', 10, 200000, 50000)

    country = st.selectbox('Country', ['France', 'Germany', 'Spain'])
    gender = st.selectbox('Gender', ['Male', 'Female'])
    is_active = st.checkbox('Is Active Member')

    df = pd.DataFrame({
        'CreditScore': [credScore],
        'Geography': [country],
        'Gender': [gender],
        'Age': [age],
        'Balance': [balance],
        'NumOfProducts': [num_products],
        'IsActiveMember': [int(is_active)],
        'EstimatedSalary': [estimated_salary]
    })
    return df

X_input = input_user()

if st.button('Predict'):
    prediction = pipeline.predict(X_input)[0]


    my_bar = st.progress(0)
    for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)

    if prediction == 1:
        st.error('⚠️ این مشتری احتمالاً **خواهد رفت**')
    else:
        st.success('✅ این مشتری احتمالاً **خواهد ماند**')