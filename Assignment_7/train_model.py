#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle


# In[2]:


# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv")


# In[3]:


df


# In[4]:


# Features and target
X = df.drop("Outcome", axis=1)
y = df["Outcome"]


# In[5]:


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[6]:


# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)


# In[7]:


# Save model
with open("diabetes_model.pkl", "wb") as f:
    pickle.dump(model, f)


# In[ ]:




