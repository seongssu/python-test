import numpy as np
import pandas as pd

class AnalyzerUpbit:
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
        self.ma_data = {}
    
        for ticker, data in self.days_candle_data.items():
            self.ma_data[ticker] = data["close"].rolling(day).mean()
        return self.ma_data
    
    def get_volatility(self, day):
        
        self.volatility_d = {}
        self.std = {}
        for ticker, data in self.days_candle_data.items():
            
            change_price = data["close"].pct_change()
            std_data = change_price.tail(day).std()
            self.std[ticker] = data["close"].tail(day).std()
            profit_day = std_data * np.sqrt(252)            
            
            self.volatility_d [ticker] = round(float(profit_day), 2)
        
        return self.volatility_d 
    
    def get_upper_band(self):
        upper_band = {}
        for ticker in self.ma_data:
            upper_band[ticker] = self.ma_data[ticker] + (self.std[ticker] * 2)
        return upper_band
    
    def get_lower_band(self):
        lower_band = {}
        for ticker in self.ma_data:
            lower_band[ticker] = self.ma_data[ticker] - (self.std[ticker] * 2) 
        return lower_band