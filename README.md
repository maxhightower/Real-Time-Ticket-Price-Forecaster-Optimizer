
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
git clone https://github.com/yourusername/ticket-pricing-optimizer.git
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

