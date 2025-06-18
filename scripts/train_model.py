import pandas as pd
from prophet import Prophet
import json
import joblib
from pathlib import Path


def train_forecast_model():
    csv_path = Path("data/raw/nfl-ticket-data.csv")
    if not csv_path.exists():
        raise FileNotFoundError("data/raw/nfl-ticket-data.csv missing – run fetch_fivethirtyeight.py first")

    df = pd.read_csv(csv_path)
    df = df.dropna(subset=["avg_price", "date"])
    df = df.rename(columns={"date": "ds", "avg_price": "y"})

    m = Prophet()
    m.fit(df[["ds", "y"]])

    future = m.make_future_dataframe(periods=30)
    forecast = m.predict(future)

    Path("reports").mkdir(exist_ok=True)
    joblib.dump(m, "reports/model.pkl")
    forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].to_csv("reports/forecast.csv", index=False)

    # naive MAE (align by date)
    actual = df.set_index("ds").reindex(forecast["ds"]).dropna()
    mae = (forecast.set_index("ds").loc[actual.index, "yhat"] - actual["y"]).abs().mean()

    with open("reports/metrics.json", "w") as f:
        json.dump({"mae": float(mae)}, f, indent=2)

    print(f"✔ Model trained – MAE: {mae:.2f} → reports/metrics.json")

if __name__ == "__main__":
    train_forecast_model()
