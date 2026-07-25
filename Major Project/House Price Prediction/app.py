import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("house_price_model.pkl", "rb"))

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 House Price Prediction")
st.write("Enter the house details below and click **Predict Price**.")

# User Inputs
bedrooms = st.number_input("Bedrooms", min_value=0, value=3)
bathrooms = st.number_input("Bathrooms", min_value=0.0, value=2.0, step=0.5)
sqft_living = st.number_input("Living Area (sqft)", min_value=0, value=2000)
sqft_lot = st.number_input("Lot Size (sqft)", min_value=0, value=5000)
floors = st.number_input("Floors", min_value=1.0, value=1.0, step=0.5)
waterfront = st.selectbox("Waterfront", [0, 1])
view = st.slider("View Rating", 0, 4, 0)
condition = st.slider("Condition", 1, 5, 3)
sqft_above = st.number_input("Sqft Above Ground", min_value=0, value=1500)
sqft_basement = st.number_input("Sqft Basement", min_value=0, value=500)
yr_built = st.number_input("Year Built", min_value=1900, max_value=2026, value=2000)
yr_renovated = st.number_input("Year Renovated (0 if never)", min_value=0, max_value=2026, value=0)
city = st.number_input("City (Encoded)", min_value=0, value=0)

if st.button("Predict Price"):

    data = np.array([[
        bedrooms,
        bathrooms,
        sqft_living,
        sqft_lot,
        floors,
        waterfront,
        view,
        condition,
        sqft_above,
        sqft_basement,
        yr_built,
        yr_renovated,
        city
    ]])

    prediction = model.predict(data)

    st.success(f"🏠 Predicted House Price: ${prediction[0]:,.2f}")