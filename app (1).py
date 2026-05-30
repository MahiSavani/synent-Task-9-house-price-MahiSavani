
import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.title("House Price Prediction")

bedrooms = st.number_input("Bedrooms", 1, 10)
bathrooms = st.number_input("Bathrooms", 1, 10)
sqft_living = st.number_input("Sqft Living")
floors = st.number_input("Floors", 1, 5)

if st.button("Predict"):
    features = np.array([[bedrooms, bathrooms, sqft_living, floors]])
    result = model.predict(features)
    st.write("Predicted Price:", result[0])
