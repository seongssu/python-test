from util_func import convert_str_to_list, retry_call_api
import pyupbit

class PyUpbitApi:
    
    def __init__(self, tickers, days):
        self.tickers = tickers
        self.days = days    
        self.retry = 3
        self.delay = 1
    
    def get_ticker_lists(self):
        result_ticker_lists = retry_call_api(pyupbit.get_tickers, self.retry, self.delay)        
        return convert_str_to_list(result_ticker_lists)
        
        
    def get_current_price(self):       
        result_current_price = retry_call_api(pyupbit.get_current_price, self.retry, self.delay, self.tickers)
        return result_current_price
        
        
        
    def get_candle_data(self):
        
        days_candle_data = {}
            
        for ticker in self.tickers:
            days_candle_data[ticker] = retry_call_api(pyupbit.get_ohlcv, self.retry, self.delay, ticker,self.days)
            
        return days_candle_data
       
        