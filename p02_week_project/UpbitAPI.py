import requests
import json

class Upbit_API:
    def __init__(self, tickers, count):
        self.tickers = tickers
        self.count = count
    # 현재가 조회 : https://docs.upbit.com/kr/reference/list-tickers
    def get_current_prices(self):
        
        url = "https://api.upbit.com/v1/ticker"
        params = {'markets' : ",".join(self.tickers)}
        headers = {'accept' : 'application/json'}
        
        response = requests.get(url, params= params, headers= headers)
        response.raise_for_status()
        current_prices = response.json()
        
        current_prices_dict = {}
        for item in current_prices:
            current_prices_dict[item["market"]] = item["trade_price"]
        
        return current_prices_dict
    
    # 페어 목록 조회 : https://docs.upbit.com/kr/reference/list-trading-pairs
    def get_krw_tickers(self):
        
        url = "https://api.upbit.com/v1/market/all"
        params = {"is_details" : False}
        headers = {'accept' : 'application/json'}
        
        response = requests.get(url, params= params, headers= headers)
        
        response.raise_for_status()
        krw_tickers_list = response.json()
        
        return krw_tickers_list
    
    # 일 캔들 조회 : https://docs.upbit.com/kr/reference/list-candles-days
    def get_candle_data(self):
        
        url = "https://api.upbit.com/v1/candles/days"
        params = {
            "market" : self.tickers,
            "count" : self.count
        }
        headers = {'accept': 'application/json'}
        
        response = requests.get(url, params=params, headers= headers)
        
        response.raise_for_status()
        candle_data = response.json()
        
        return candle_data
        