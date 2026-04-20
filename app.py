from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Prediction
@app.route("/predict", methods=["POST"])
def predict():
    value = float(request.form["value"])
    prediction = model.predict([[value]])
    return render_template("index.html",
                           result=f"Predicted Output: {prediction[0]}")

# Run app
if __name__ == "__main__":
    app.run(debug=True)