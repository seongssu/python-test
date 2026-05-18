from remote.except_call import retry_call_api
import pyupbit
from remote.cache_manager import CacheManager

class PyUpbitApi:
    
    def __init__(self, tickers, days):
        self.tickers = tickers
        self.days = days    
        self.retry = 3
        self.delay = 1
        self.cache_manager = CacheManager()
    
    def get_ticker_lists(self):
        result_ticker_lists = retry_call_api(pyupbit.get_tickers, self.retry, self.delay)        
        return list(result_ticker_lists)
        
        
    def get_current_price(self):       
        result_current_price = retry_call_api(pyupbit.get_current_price, self.retry, self.delay, self.tickers)
        return result_current_price
        
        
        
    def get_candle_data(self, table_name):
        
        days_candle_data = {}
            
        for ticker in self.tickers:
            
            if self.cache_manager.get_cache(ticker, table_name):
                print(f"캐시가 존재합니다 : {ticker}")
                days_candle_data[ticker] = self.cache_manager.load_cache(ticker, table_name)
                continue
            
            print(f"API를 호출합니다 : {ticker}")
                
            days_candle_data[ticker] = retry_call_api(pyupbit.get_ohlcv, self.retry, self.delay, ticker, count = self.days + 1)
            days_candle_data[ticker].index.name = "date"            
        
        return days_candle_data
       
        