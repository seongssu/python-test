import requests
from datetime import datetime
import time
import json
import pandas as pd

def get_candle_data_api(ticker, count):
    
    #url 끝에 공백이 들어가면 안된다. 잘못된 주소로 요청함
    url = "https://api.upbit.com/v1/candles/days"
    headers = {"accept": "application/json"}
    params = {
        "market" : ticker,
        "count" : count 
    }
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    
    return data

ticker = "KRW-BTC"
count = 30

data = get_candle_data_api(ticker, count)

prices_date = []

for item in data:      
    date = item['candle_acc_trade_volume']
    prices = item['trade_price']

    #print(f"종가 : {prices}, 날짜 : {date} ")
    
    prices_date.append([date, prices])

#print(f"날짜 종가 리스트 : {prices_date}")
pd_prices_date = pd.DataFrame(prices_date)
print(pd_prices_date)