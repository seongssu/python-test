import requests
from datetime import datetime
import time
import json

def get_single_price_api(ticker):
    url = "https://api.upbit.com/v1/ticker"
    headers = {"accept": "application/json"}

    params = {"markets": ticker}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()[0]
    return data['trade_price']

ticker = "KRW-BTC"
get_single_price_api(ticker)
print(f"뭐야이건{get_single_price_api(ticker)}")