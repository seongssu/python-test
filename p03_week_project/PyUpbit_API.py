from util_func import convert_str_to_list
import pyupbit

class PyUpbit_Api:
    
    def __init__(self, tickers, days):
        self.tickers = tickers
        self.days = days    
    
    def get_ticker_lists(self):        
        
        try:
            return convert_str_to_list(pyupbit.get_tickers())
            
        except Exception as e:
            print(f"ERROR : {e}")
            return None
        
    def get_current_price(self):
        
        try:
            return pyupbit.get_current_price(self.tickers)
        
        except Exception as e:
            print(f"Error : {e}")
            return None
        
    def get_candle_data(self):
        
        try:
            days_candle_data = {}
            
            for ticker in self.tickers:
                days_candle_data[ticker] = pyupbit.get_ohlcv(ticker)
            
            return days_candle_data
        
        except Exception as e:
            print(f"ERROR : {e}")
            return None
        