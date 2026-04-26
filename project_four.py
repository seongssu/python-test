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

    return candle_data[-1]["trade_price"]

#비교할 암호화폐 목록(리스트)
tickers = ["KRW-BTC", "KRW-ETH", "KRW-XRP", "KRW-SOL"]
days_ago = 30

#호출 함수에서 ticker가 str타입으로 받아야해서 for문 돌림
for item in tickers:
    print(f"잘 작동하나? {get_historical_close_api(item, days_ago)}")
    