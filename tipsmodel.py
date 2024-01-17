import streamlit as st
import joblib
st.markdown("<h1 style='text-align:center'>Bill Prediction</h1>",unsafe_allow_html=True)
st.markdown("<h3  style='text-align:center'>Shows the total bill paid</h3>",unsafe_allow_html=True)
tip=st.number_input("Enter the tip paid",min_value=0)
sex=st.radio("select your gender",["male","female"],horizontal=True)
smoker=st.selectbox("smoker?",["yes","no"])
time=st.selectbox("Enter the time",["day","night"])
size=st.number_input("enter size of your family",min_value=0)
if sex == "male":
    sex=1
else:
    sex=0
if smoker == "yes":
    smoker=1
else:
    smoker=0
if time == "day":
    time=0
else:
    time=1



if st.button("predict"):
    model=joblib.load("tips model.h5")
    prediction=model.predict([[tip,sex,smoker,time,size]])
    st.success(prediction[0])