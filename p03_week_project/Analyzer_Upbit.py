import numpy as np
import pandas as pd

class Analyzer_Upbit:
    def __init__(self, current_price, days_candle_data):
        self.current_price = current_price
        self.days_candle_data = days_candle_data

    def get_return_rate_d(self, days_ago):
        
        return_rate_d = {}
        for ticker, current_price in self.current_price.items():
            
            df = self.days_candle_data[ticker]
            days_ago_price = df.iloc[-(days_ago + 1)]["close"]
            
            days_age_profit_rate = ((current_price - days_ago_price) / days_ago_price) * 100
            
            
            return_rate_d[ticker] = round(float(days_age_profit_rate), 2)
        return return_rate_d
    
    def get_ma(self, day):
        ma_data = {}
    
        for ticker, data in self.days_candle_data.items():
            ma_data[ticker] = data["close"].rolling(day).mean()
        return ma_data
    
    def get_volatility(self, day):
        
        volatility_d = {}
        for ticker, data in self.days_candle_data.items():
            
            change_price = data["close"].pct_change()
            profit_day = change_price.tail(20).std() * np.sqrt(252)
            
            volatility_d[ticker] = round(float(profit_day), 2)
        
        return volatility_d