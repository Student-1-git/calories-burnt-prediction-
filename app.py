from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("calories_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        gender = request.form["gender"]
        age = float(request.form["age"])
        height = float(request.form["height"])
        weight = float(request.form["weight"])
        duration = float(request.form["duration"])
        heart_rate = float(request.form["heart_rate"])
        body_temp = float(request.form["body_temp"])

        # Convert gender to numerical
        gender = 0 if gender.lower() == "male" else 1

        # Format for model prediction
        features = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])
        prediction = model.predict(features)[0]

        return render_template("index.html", prediction_text=f"Calories Burnt: {prediction:.2f} kcal")

if __name__ == "__main__":
    app.run(debug=True)
