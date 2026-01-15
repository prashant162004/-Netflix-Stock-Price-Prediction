# 📈 Netflix Stock Price Prediction

This project predicts the **Netflix (NFLX) stock price** using **Machine Learning** based on historical stock market data.  
It includes a **trained ML model** and a **Flask web application** for user interaction.

---

## 🚀 Features
- Predicts Netflix stock price using historical data
- Machine Learning model trained on real stock data
- Flask-based web interface
- User-friendly input form
- Fast and accurate predictions

---

## 🧠 Machine Learning Approach
- Data preprocessing and feature selection
- Supervised Machine Learning model
- Model trained using historical Netflix stock data
- Model saved using Pickle (`model.pkl`)

---

## 📂 Project Structure
Netflix-Price-Prediction/
│
├── app.py # Flask application
├── model.pkl # Trained ML model
├── NFLX.csv # Dataset
├── Netflix_Peice_Prediction.ipynb # Jupyter Notebook (Model training)
├── templates/
│ └── index.html # Frontend HTML file
├── README.md # Project documentation

yaml
Copy code

---

## 📊 Input Features
The model uses the following inputs:
- Open Price
- High Price
- Low Price
- Adjusted Close Price
- Volume
- Year
- Month
- Day

---

## 🛠️ Tech Stack
- Python
- Machine Learning
- NumPy
- Flask
- Pickle
- HTML/CSS

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Netflix-Price-Prediction.git
cd Netflix-Price-Prediction
2️⃣ Install Required Libraries
bash
Copy code
pip install flask numpy
3️⃣ Run the Flask App
bash
Copy code
python app.py
4️⃣ Open in Browser
cpp
Copy code
http://127.0.0.1:5000/
📌 Output
The application predicts and displays the Netflix stock price based on the user inputs.

📈 Future Improvements
Add real-time stock data API

Improve model accuracy using advanced algorithms

Deploy the application on cloud platforms (Heroku / AWS)
