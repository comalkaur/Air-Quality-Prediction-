# 🍃 Air Quality Prediction System

A Machine Learning-based Air Quality Prediction System that predicts the **Air Quality Index (AQI)** using environmental and pollutant parameters. The project integrates a trained Machine Learning model with a Flask web application and a modern dashboard interface for real-time AQI prediction.

---

## 📌 Project Overview

Air pollution has become one of the major environmental concerns worldwide. This project predicts the Air Quality Index (AQI) based on various pollutant concentrations and environmental conditions.

The system uses Machine Learning algorithms to analyze air quality data and provides AQI predictions along with the corresponding air quality category.

---

## 🚀 Features

- Predict Air Quality Index (AQI)
- Machine Learning-based prediction model
- Flask web application
- Interactive and responsive dashboard UI
- AQI category classification
- Input validation and error handling
- Modern user interface
- Real-time AQI prediction

---

## 📊 Input Parameters

The model predicts AQI using the following parameters:

- PM2.5 (µg/m³)
- PM10 (µg/m³)
- NO₂ (ppb)
- SO₂ (ppb)
- CO (ppm)
- O₃ (ppb)
- Temperature (°C)
- Humidity (%)
- Wind Speed (km/h)

---

## 🧠 Machine Learning Model

The project uses Machine Learning techniques for AQI prediction.

### Algorithms Used

- Linear Regression
- Decision Tree Regression
- Random Forest Regression

The best-performing model is saved using:

- Joblib
- Pickle

---

## 🛠️ Technologies Used

### Backend
- Python
- Flask

### Machine Learning
- Scikit-Learn
- Pandas
- NumPy

### Frontend
- HTML5
- CSS3
- Jinja2

---

## 📁 Project Structure

```text
air_quality_project/
│
├── app.py
├── air_quality.py
├── model.pkl
├── scaler.pkl
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/air-quality-prediction.git

cd air-quality-prediction
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## 📈 AQI Categories

| AQI Range | Category |
|----------|-----------|
| 0 – 50 | Good |
| 51 – 100 | Moderate |
| 101 – 150 | Unhealthy for Sensitive Groups |
| 151 – 200 | Unhealthy |
| 201 – 300 | Very Unhealthy |
| 301+ | Hazardous |

---

## 💻 User Interface

The application provides:

- Responsive Dashboard
- AQI Prediction Form
- AQI Category Indicator
- Modern Card-Based Layout
- AQI Scale Visualization

---

## 🔮 Future Improvements

- Real-time AQI API integration
- Historical prediction tracking
- Data visualization charts
- User authentication system
- Cloud deployment
- Location-based AQI prediction

----

## 🤝 Contribution

Contributions, suggestions, and improvements are welcome.

Feel free to fork this repository and submit pull requests.

---

## 👩‍💻 Author

**Komalpreet Kaur**

---

## 📄 License

This project is developed for educational and learning purposes.

