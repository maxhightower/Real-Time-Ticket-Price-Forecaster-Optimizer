import pandas as pd

class PriceOptimizer:
    def __init__(self, elasticity=-1.2):
        self.elasticity = elasticity

    def optimal_price(self, current_price, demand_ratio):
        return current_price * (1 + demand_ratio / self.elasticity)

    def apply_strategy(self, df):
        df["recommended_price"] = df.apply(
            lambda row: self.optimal_price(row["current_price"], row["demand_ratio"]), axis=1
        )
        return df
