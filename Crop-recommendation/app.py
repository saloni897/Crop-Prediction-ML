from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        nitrogen = float(request.form["Nitrogen"])
        phosphorus = float(request.form["Phosphorus"])
        potassium = float(request.form["Potassium"])
        temperature = float(request.form["Temperature"])
        humidity = float(request.form["Humidity"])
        ph = float(request.form["pH"])
        rainfall = float(request.form["Rainfall"])

        features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
        prediction = model.predict(features)[0]

        return render_template("index.html", prediction_text=f"Recommended Crop: {prediction}")

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)