<h1 align="center">🔮 Customer Churn Prediction – ML + API Deployment</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit--learn-1.6.1-orange?logo=scikit-learn" />
  <img src="https://img.shields.io/badge/Flask-API-green?logo=flask" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Production-red" />
  <img src="https://img.shields.io/badge/Deployment-Render-purple?logo=render" />
  <img src="https://img.shields.io/github/license/yeswu/churn-prediction" />
</p>



🚀 Overview

A fully production-ready **Customer Churn Prediction System** built using  
**Python, Scikit-learn, Flask, and Render**.  

The project includes:

- End-to-end data preprocessing  
- Feature engineering using `ColumnTransformer`  
- Automated model comparison  
- Saving the best ML model  
- Deploying to Render as a scalable REST API  
- Real-time churn prediction using JSON input  

This project is designed with enterprise-ready architecture, making it clean, modular, and deployment-focused.


 📦 Tech Stack

| Category | Technologies |
|---------|--------------|
| **Language** | Python 3.10+ |
| **ML Framework** | Scikit-learn 1.6.1 |
| **API Framework** | Flask |
| **Deployment** | Render |
| **Model Handling** | joblib |
| **Data Processing** | pandas, numpy |


📂 Project Structure
├── app.py # Flask API
├── best_churn_model.pkl # Saved best ML model
├── requirements.txt # Dependencies
├── Procfile # Render startup command
├── README.md # Project documentation
└── .gitignore # Files to ignore in repo



🧠 How It Works

🔍 1. Data Preprocessing
- Handles missing values  
- Encodes categorical columns using OneHotEncoder  
- Scales numeric features using StandardScaler  

 🤖 2. Model Training
Compares:
- Logistic Regression  
- Random Forest  
- Gradient Boosting  

Best model selected using **F1-Score** (ideal for imbalanced churn datasets).

🧩 3. Model Saving
The final best model is stored as:
best_churn_model.pkl


🌐 4. Deployment
- Deployed on **Render Web Service**
- Runs using Gunicorn
- Exposes a REST API for predictions  
rements.txt
