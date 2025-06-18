import pandas as pd
from prophet import Prophet
import json
import joblib
import os

def train_forecast_model():
    df = pd.read_csv("data/raw/nfl-ticket-data.csv")
    df = df.dropna(subset=["avg_price", "date"])
    df = df.rename(columns={"date": "ds", "avg_price": "y"})
    
    model = Prophet()
    model.fit(df[["ds", "y"]])

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    os.makedirs("reports", exist_ok=True)
    joblib.dump(model, "reports/model.pkl")
    forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].to_csv("reports/forecast.csv", index=False)
    
    mae = (forecast["yhat"] - df.set_index("ds").reindex(forecast["ds"])["y"]).abs().mean()
    with open("reports/metrics.json", "w") as f:
        json.dump({"mae": mae}, f, indent=2)

if __name__ == "__main__":
    train_forecast_model()
