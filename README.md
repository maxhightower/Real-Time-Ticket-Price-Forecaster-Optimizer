# Project: ticket-pricing-optimizer
Description: Real-time ticket price forecasting and dynamic optimization using public sports event data

## Directory structure reference:

.
├── README.md
├── environment.yml
├── data/
│   ├── raw/
│   └── processed/
├── scripts/
│   ├── fetch_seatgeek.py
│   ├── build_sqlite.py
│   ├── train_model.py
│   └── price_optimizer.py
├── notebooks/
│   └── demo.ipynb
├── reports/
│   └── metrics.json
├── .github/workflows/
│   ├── retrain.yml
│   └── pages.yml
└── tests/
    └── test_optimizer.py
