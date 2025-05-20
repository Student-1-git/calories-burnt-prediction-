# Calories Burnt Prediction Web App
This is a machine learning-powered web application that predicts the number of calories burnt during physical activity. Users can input personal details like age, gender, height, weight, and duration of activity, and receive an estimated calorie burn value.
The app is built using an XGBoost Regressor model and deployed with a Flask backend, featuring a simple HTML/CSS frontend.

📌Project Overview
Model: XGBoost Regressor
Framework: Flask
Language: Python
Frontend: HTML, CSS
IDE: Visual Studio Code

Machine Learning Model
Algorithm: XGBoost Regressor
Training Data Features:
Gender
Age
Height (cm)
Weight (kg)
Duration (minutes)
Output: Predicted Calories Burnt

Folder Structure

calorie-predictor-webapp/
├── app.py                 # Flask backend logic
├── model.pkl              # Trained XGBoost model
├── templates/
│   └── index.html         # Input form for user data
├── static/
│   └── style.css          # Frontend styling
├── requirements.txt       # List of Python dependencies
└── README.md              # Project overview and setup

Dependencies
Here's a list of packages required:
Flask
pandas
numpy
xgboost
scikit-learn
These are already listed in the requirements.txt file. 

Installation and Setup
1. Clone the repository

2. (Optional) Create a virtual environment:
   python -m venv venv

3. Activate the virtual environment:
   - On Windows:
       venv\Scripts\activate
   - On macOS/Linux:
       source venv/bin/activate

4. Install required packages:
   pip install -r requirements.txt

5. Get the trained model file (model.pkl):
   - If 'model.pkl' is included in the repo, you’re good to go.
   - Otherwise,
   - Save the Model as model.pkl
In your training script (the Python file where you train your model), add this code at the end:
import pickle
  suppose your trained model is called 'model'
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model saved successfully as model.pkl")
This will save the trained XGBoost Regressor model as a model.pkl file in your project directory.
Make sure the model.pkl file is in the same folder as your app.py file (Flask backend). Your Flask app will load this file to make predictions.


6. Run the Flask application:
   python app.py

7. Open your browser and visit:

Example Input and Output

Example
Gender:	Male
Age:	25
Height: (cm)	170
Weight: (kg)	65
Duration: (min)	30
➡️ Output: Estimated calories burnt: 245 kcal (example)
   





