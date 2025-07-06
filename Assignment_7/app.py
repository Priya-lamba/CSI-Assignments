#!/usr/bin/env python
# coding: utf-8

# In[41]:


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle


# In[42]:


# Load trained model
with open("diabetes_model.pkl", "rb") as f:
    model = pickle.load(f)


# In[43]:


# App title and instructions
st.title("Diabetes Prediction App")
st.write("Enter your health data to predict if you're likely to have diabetes.")


# In[44]:


# TEMP: Skip model load to test UI only
#st.title("Test: Diabetes Prediction UI")


# In[45]:


# Input form
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.slider("Glucose Level", 0, 200, 100)
bp = st.slider("Blood Pressure", 0, 150, 70)
skin_thickness = st.slider("Skin Thickness", 0, 100, 20)
insulin = st.slider("Insulin", 0, 900, 80)
bmi = st.slider("BMI", 0.0, 70.0, 25.0)
dpf = st.slider("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
age = st.slider("Age", 10, 100, 33)


# In[46]:


# Combine into single row
input_data = np.array([[pregnancies, glucose, bp, skin_thickness, insulin, bmi, dpf, age]])


# In[47]:


# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][prediction]

    if prediction == 1:
        st.error(f" High Risk of Diabetes (Probability: {prob:.2f})")
    else:
        st.success(f" Low Risk of Diabetes (Probability: {prob:.2f})")


# In[ ]:





# In[ ]:




