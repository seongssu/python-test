import requests
from datetime import datetime
import time
import json

import requests

def get_historical_close_api(ticker, days_ago):
    url = "https://api.upbit.com/v1/candles/days"

    params = {
        "market": ticker,
        "count": days_ago
    }

    response = requests.get(url, params=params)
    candle_data = response.json()
    
    current_price = candle_data[0]["trade_price"]
    past_price = candle_data[-1]["trade_price"]

    return {
        "current_price": current_price, 
        "past_price": past_price
        }

#비교할 암호화폐 목록(리스트)
tickers = ["KRW-BTC", "KRW-ETH", "KRW-XRP", "KRW-SOL"]
days_ago = 30

current_past = {}
#호출 함수에서 ticker가 str타입으로 받아야해서 for문 돌림
for item in tickers:
    price = get_historical_close_api(item, days_ago)
    current_past[item] = price

print(f"현재가와 과거가격: {current_past}")