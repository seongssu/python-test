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

price = get_candle_data_api(ticker, count)

print(f"무슨데이터일까 {price}")