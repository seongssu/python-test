import requests
from datetime import datetime
import time
import json
import pandas as pd
import matplotlib.pyplot as plt

def get_current_prices_api(tickers):

    url = "https://api.upbit.com/v1/ticker"
    headers = {"accept": "application/json"}

    markets_param = ",".join(tickers)
    params = {"markets": markets_param}

    response = requests.get(url, headers=headers, params=params)
    prices_data = response.json()

    prices = {}
    for data in prices_data:
        prices[data['market']] = data['trade_price']

    return prices

def get_historical_close_api(portfolio, days_ago):
    url = "https://api.upbit.com/v1/candles/days"

    result = {}
    for ticker in portfolio:
        params = {
            "market": ticker,
            "count": days_ago
        }

        response = requests.get(url, params=params)
        candle_data = response.json()

        current_price = candle_data[0]["trade_price"]
        past_price = candle_data[-1]["trade_price"]

        result[ticker] = {
            "current_price" : current_price,
            "past_price" : past_price
        }


    return result

def get_candle_data_api(ticker, count):

    url = "https://api.upbit.com/v1/candles/days"
    headers = {"accept": "application/json"}
    params = {
        "market" : ticker,
        "count" : count
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    return data