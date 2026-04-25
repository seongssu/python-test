import requests
from datetime import datetime
import time
import json

def get_historical_data_api(ticker, days_count):
    url = "https://api.upbit.com/v1/candles/days"

    params = {
        "market": ticker,
        "count": days_count
    }

    response = requests.get(url, params=params)
    candle_data = response.json()

    prices = []

    for data in candle_data:
        prices.append(data["trade_price"])

    return prices

ticker = "KRW_BTC"
day_invest = 30
money_invest = 100