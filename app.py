from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("best_churn_model.pkl")

@app.route("/")
def home():
    return {"message": "Customer Churn Prediction API is running 🎯"}

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        df = pd.DataFrame([data])

        pred = model.predict(df)[0]

        # Check if model supports predict_proba
        if hasattr(model, "predict_proba"):
            proba = float(model.predict_proba(df)[0][1])
        else:
            proba = None

        return jsonify({
            "prediction": int(pred),
            "confidence": proba
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
