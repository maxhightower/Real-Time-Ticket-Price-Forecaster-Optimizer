
# Ticket Pricing Optimizer

Forecast sports ticket prices and optimize pricing dynamically using open data and Python.

## Features
- Ingests public data from FiveThirtyEight and SeatGeek API
- Forecasts ticket prices using Prophet
- Optimizes price recommendations with a simple elasticity model
- SQLite backend for local, lightweight analysis
- GitHub Actions for retraining and metric tracking

## Setup
```bash
git clone https://github.com/maxhightower/ticket-pricing-optimizer.git
cd ticket-pricing-optimizer
conda env create -f environment.yml
```

## Run
```bash
python scripts/fetch_seatgeek.py
python scripts/build_sqlite.py
python scripts/train_model.py
pytest tests/
```

## License
MIT

# Ticket Pricing Optimizer (Updated)

## Quickstart (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
# 1️⃣ Download data
python scripts/fetch_fivethirtyeight.py   # public NFL ticket data
$env:SEATGEEK_CLIENT_ID="YOUR_FREE_CLIENT_ID"   # optional but recommended
python scripts/fetch_seatgeek.py          # live event snapshot
# 2️⃣ Build DB, train model, run tests
python scripts/build_sqlite.py
python scripts/train_model.py
pytest -q
```
If SeatGeek returns 403, register a free developer account and set `SEATGEEK_CLIENT_ID` as shown above.
