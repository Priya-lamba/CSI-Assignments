 # 🩺 Diabetes Prediction App (Streamlit + Machine Learning)

This is a web application built using **Streamlit** and a trained **Random Forest Classifier** to predict the risk of diabetes based on user health parameters.

---

## 🔧 Features

- Accepts user input for medical parameters (like Glucose, BMI, Age, etc.)
- Predicts diabetes risk using a trained ML model
- Shows prediction probability
- Simple and interactive UI using Streamlit

---


## 🚀 How to Run This Project

### 1. clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/diabetes-prediction-app.git
cd diabetes-prediction-app
---

### 2. Install requirements
pip install -r requirements.txt

---
### 3. Train the model (creates diabetes_model.pkl)
python train_model.py

---
### 4. Run the Streamlit app
streamlit run app.py

---
📊 Example Inputs
Glucose: 120

BMI: 28.5

Age: 45

...

The app will show whether you're at high or low risk of diabetes with a probability score.
---



