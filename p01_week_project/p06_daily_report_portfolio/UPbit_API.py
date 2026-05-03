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
        self.get_profit_max_coin(result)
        
        return result
    
    def get_profit_max_coin(self,result):
        
        profit_rate = []
        for ticker, price in result.items():
            #print(f"ticker {ticker}, price {price}")
            today = price["current_price"]
            past = price["past_price"]
            
            profit_ratio = ((today - past) / past) * 100
            
            profit_rate.append({
                "ticker": ticker,
                "profit": profit_ratio
            })
        # max( 데이터, key=lambda x: x["키값"]) : max함수의 딕셔너리 활용  
        coin_profit = max(profit_rate, key=lambda x: x["profit"])
        print(f"최고수익코인 : {coin_profit["ticker"]}")

        #4 특정 코인 1개의 최근 7일 가격 추이 그래프

        #ticker_item = "KRW-BTC"

        coin_price_change = self.get_candle_data_api()

        coin_price_change = coin_price_change[::-1]
        coin_price = []
        coin_date = []

        for item in coin_price_change:
            date = item["candle_date_time_kst"]
            price = item["trade_price"]
            
            coin_price.append(price)
            coin_date.append(date)

        #print(f"날짜가격 : {coin_date}")
        plt.plot(coin_date,coin_price, label="MA7")
        plt.show()
        

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