import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
data = {
    'Area': [1000, 1500, 2000, 2500, 3000],
    'Bedrooms': [2, 3, 3, 4, 4],
    'Price': [3000000, 4500000, 5000000, 6500000, 8000000]
}
df = pd.DataFrame(data)
X = df[['Area', 'Bedrooms']]
y = df['Price']
model = LinearRegression()
model.fit(X, y)
st.title("🏠 House Price Prediction")
area = st.number_input("Enter Area")
bedrooms = st.number_input("Enter Bedrooms")
if st.button("Predict Price"):
    prediction = model.predict([[area, bedrooms]])
    st.success(f"Estimated Price: ₹{prediction[0]:,.0f}")
