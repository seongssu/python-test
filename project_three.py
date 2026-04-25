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

def get_single_price_api(ticker):
    url = "https://api.upbit.com/v1/ticker"

    params = {
        "markets": ticker
    }

    response = requests.get(url, params=params)

    data = response.json()[0]
    return data['trade_price']

def calculate_investment_return(money_invest, ticker, day_invest):
    print(f"뭐가나오나{get_historical_data_api(ticker, day_invest)}")


ticker = "KRW-BTC"
day_invest = 30
money_invest = 1000000

calculate_investment_return(1000000,ticker, day_invest)