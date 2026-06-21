from flask import Flask,render_template,request
import joblib
import numpy as np

app=Flask(__name__)

model=joblib.load("aqi_prediction_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():

    data=[
    float(request.form["pm25"]),
    float(request.form["pm10"]),
    float(request.form["no2"]),
    float(request.form["so2"]),
    float(request.form["co"]),
    float(request.form["o3"]),
    float(request.form["temperature"]),
    float(request.form["humidity"]),
    float(request.form["wind_speed"]),
    float(request.form["pressure"]),
    ]

    prediction=model.predict([data])[0]

    if prediction<=50:
        category="Good"
    elif prediction<=100:
        category="Moderate"
    elif prediction<=200:
        category="Unhealthy"
    else:
        category="Very Unhealthy"

    return render_template(
        "index.html",
        prediction=round(prediction,2),
        category=category
    )

if __name__=="__main__":
    app.run(debug=True)