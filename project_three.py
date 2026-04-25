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
    #과거투자시점 가격
    money_past = get_historical_data_api(ticker, day_invest)
    volumes = money_invest / money_past[-1]
    print(f"구매량: {volumes}")
    
    
ticker = "KRW-BTC"
day_invest = 30
money_invest = 1000000

calculate_investment_return(money_invest, ticker, day_invest)