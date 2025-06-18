import pandas as pd
from scripts.price_optimizer import PriceOptimizer

def test_optimal_price():
    po = PriceOptimizer(elasticity=-1.5)
    price = po.optimal_price(100, 0.2)
    assert round(price, 2) == 86.67

def test_apply_strategy():
    po = PriceOptimizer()
    df = pd.DataFrame({"current_price": [100], "demand_ratio": [0.1]})
    result = po.apply_strategy(df)
    assert "recommended_price" in result.columns
