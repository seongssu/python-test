from util_func import convert_str_to_list, retry_call_api
import pyupbit
from cache_manager import CacheManager

class PyUpbitApi:
    
    def __init__(self, tickers, days, category):
        self.tickers = tickers
        self.days = days    
        self.retry = 3
        self.delay = 1
        self.cache_manager = CacheManager()
        self.category = category
    
    def get_ticker_lists(self):
        result_ticker_lists = retry_call_api(pyupbit.get_tickers, self.retry, self.delay)        
        return convert_str_to_list(result_ticker_lists)
        
        
    def get_current_price(self):       
        result_current_price = retry_call_api(pyupbit.get_current_price, self.retry, self.delay, self.tickers)
        return result_current_price
        
        
        
    def get_candle_data(self):
        
        days_candle_data = {}
            
        for ticker in self.tickers:
            
            if self.cache_manager and self.cache_manager.get_cache(ticker, self.category):
                print(f"캐시가 존재합니다 : {ticker}")
                days_candle_data[ticker] = self.cache_manager.load_cache(ticker, self.category)
                continue
            
            print(f"API를 호출합니다 : {ticker}")
            
            days_candle_data[ticker] = retry_call_api(pyupbit.get_ohlcv, self.retry, self.delay, ticker,self.days)
            days_candle_data[ticker].index.name = "date"
            days_candle_data[ticker]["category"] = self.category
        
        return days_candle_data
       
        