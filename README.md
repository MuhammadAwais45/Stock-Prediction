# 📈 Stock Price Prediction App  

## 📌 Overview  
This project is a **machine learning + GUI application** that predicts the **closing price of a stock** based on user-provided values.  
It uses **historical stock market data** fetched via Yahoo Finance and applies **Ridge Regression** for prediction.  

The aim of this project is to:  
- Collect real-world financial data  
- Train a regression model to predict stock prices  
- Build a user-friendly **Tkinter** interface for predictions  

---

## 📂 Dataset  
The dataset is fetched automatically using the [`yfinance`](https://pypi.org/project/yfinance/) library.  
In this version, we use **Apple Inc. (AAPL)** stock data for the last **6 months**, containing:  

- **Open Price**  
- **High Price**  
- **Low Price**  
- **Close Price** (target variable)  
- **Volume**  

---

## 🛠️ Technologies Used  
- **Python 3**  
- **Tkinter** — for GUI interface  
- **Pandas** — data handling  
- **Scikit-learn** — model training & evaluation  
- **yfinance** — stock data retrieval  

---

## 📊 Key Steps in Project  
1. **Data Collection**  
   Downloaded Apple (AAPL) stock data for the past 6 months.  

2. **Feature Selection**  
   Used `High`, `Low`, `Open`, and `Volume` as input features.  

3. **Data Splitting**  
   - 60% Training  
   - 20% Validation  
   - 20% Testing  

4. **Model Training**  
   Applied **Ridge Regression** with `alpha=0.01`.  

5. **GUI Development**  
   Built a **Tkinter** interface where users enter `High`, `Low`, `Open`, and `Volume` values to get a predicted `Close` price.  

---

## 📷 Sample GUI  
Enter Stock Data
High: []
Low: []
Open: []
Volume: []
[ Predict ]
Predicted Close Price: $XXX.XX 


---

## 🚀 How to Run  
1. Clone this repository:  
   ```bash
   git clone https://github.com/MuhammadAwais45/Stock-Prediction.git
   cd Stock-Prediction
   
Install dependencies:
```bash
  pip install pandas scikit-learn yfinance
```
Run the application:
```bash
  python task2.py
```
  
📌 Future Improvements
  Add multiple stock ticker options instead of just AAPL
  Implement more advanced ML models (Random Forest, XGBoost, LSTMs)
  Display prediction accuracy and historical trend charts in the GUI

