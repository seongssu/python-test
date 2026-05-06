import pandas as pd

class Analyzer_Upbit:
    
    def __init__(self, df_multi_candle_prices):
        self.df_multi_candle_prices = df_multi_candle_prices
    
    def get_price_change(self):
        self.df_multi_candle_prices["price_change"] = self.df_multi_candle_prices["opening_price"] - self.df_multi_candle_prices["trade_price"]
        print(f"{self.df_multi_candle_prices[["market", "price_change"]]}")