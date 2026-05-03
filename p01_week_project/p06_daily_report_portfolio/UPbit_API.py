import requests
from datetime import datetime
import time
import json
import pandas as pd
import matplotlib.pyplot as plt

class UPbit:
    def __init__(self, tickers, days_ago):
        self.tickers = tickers
        self.ticker = tickers[0]
        self.days_ago = days_ago 

    def get_historical_close_api(self):
        url = "https://api.upbit.com/v1/candles/days"

        result = {}
        for ticker in self.tickers:
            params = {
                "market": ticker,
                "count": self.days_ago
            }

            response = requests.get(url, params=params)
            candle_data = response.json()

            current_price = candle_data[0]["trade_price"]
            past_price = candle_data[-1]["trade_price"]
            ticker_name = ticker.split("-")[1]
            result[ticker_name] = {
                "current_price" : current_price,
                "past_price" : past_price
            }


        return result

    def get_candle_data_api(self):

        url = "https://api.upbit.com/v1/candles/days"
        headers = {"accept": "application/json"}
        params = {
            "market" : self.ticker,
            "count" : self.days_ago
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        return data