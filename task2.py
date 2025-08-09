import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# ======== Train Model (Replace this with your own dataset loading) ========
import yfinance as yf
data = yf.download("AAPL", period="6mo")[["Open", "High", "Low", "Close", "Volume"]]
X = data[["High", "Low", "Open", "Volume"]]
y = data["Close"]

# Train/Val/Test split
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, shuffle=False)

# Ridge Regression model
model = Ridge(alpha=0.01)
model.fit(X_train, y_train)
# ==========================================================================

# ======== GUI =========
def predict():
    try:
        high = float(entry_high.get())  # pyright: ignore[reportUndefinedVariable]
        low = float(entry_low.get())   # pyright: ignore[reportUndefinedVariable]
        open_ = float(entry_open.get())  # pyright: ignore[reportUndefinedVariable]
        volume = float(entry_volume.get()) # pyright: ignore[reportUndefinedVariable]

        new_data = pd.DataFrame([[high, low, open_, volume]],
                                columns=["High", "Low", "Open", "Volume"])
        pred_close = model.predict(new_data)[0]
        result_label.config(text=f"Predicted Close Price: ${pred_close:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

app = tk.Tk()
app.title("Stock Close Price Predictor")
app.geometry("400x350")

tk.Label(app, text="Enter Stock Data", font=("Arial", 14)).pack(pady=10)

fields = [("High", "entry_high"), ("Low", "entry_low"),
          ("Open", "entry_open"), ("Volume", "entry_volume")]
for label_text, var_name in fields:
    tk.Label(app, text=label_text).pack()
    entry = tk.Entry(app)
    entry.pack()
    globals()[var_name] = entry  # dynamically create entry variables

tk.Button(app, text="Predict", command=predict, bg="blue", fg="white").pack(pady=10)
result_label = tk.Label(app, text="", font=("Arial", 12))
result_label.pack(pady=10)

app.mainloop()
