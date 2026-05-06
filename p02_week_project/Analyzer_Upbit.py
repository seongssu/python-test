import pandas as pd

class Analyzer_Upbit:
    
    def __init__(self, df_multi_candle_prices):
        self.df_multi_candle_prices = df_multi_candle_prices
    
    def get_price_change(self):
        self.df_multi_candle_prices["price_change"] = self.df_multi_candle_prices["trade_price"] - self.df_multi_candle_prices["opening_price"]
        return self.df_multi_candle_prices["price_change"]
        
    def get_price_change_pct(self):
        self.df_multi_candle_prices["price_change_pct"] = (self.df_multi_candle_prices["price_change"] / self.df_multi_candle_prices["opening_price"]) * 100
        return self.df_multi_candle_prices["price_change_pct"]    
    
    def get_high_low_diff(self):
        self.df_multi_candle_prices["high_low_diff"] = self.df_multi_candle_prices["high_price"] - self.df_multi_candle_prices["low_price"]
        return self.df_multi_candle_prices["high_low_diff"]