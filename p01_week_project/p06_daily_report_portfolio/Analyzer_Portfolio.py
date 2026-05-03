import requests
from datetime import datetime
import time
import json
import pandas as pd
import matplotlib.pyplot as plt

class Analyzer_Portfolio:
    def __init__(self, portfolio, prices):
        self.portfolio = portfolio
        self.tickers = list(portfolio.keys())
        self.prices = prices
    def analyze_portfolio(self):

        #tickers = list(self.portfolio.keys())
        
        #prices = self.get_current_prices_api()

        portfolio_analysis = []
        total_value = 0

        for stocks, volumes in self.portfolio.items():

            current_price = self.prices.get(stocks,0)
            value = current_price * volumes

            portfolio_analysis.append({
                "코인" : stocks,
                "수량" : volumes,
                "현재가격" : current_price,
                "가치" : value
        })

            total_value += value

        for x in portfolio_analysis:
            x["비중"] = (x["가치"]/total_value) * 100
        
        self.portfolio_analysis = portfolio_analysis
        
        return portfolio_analysis
    
    def get_max_coin(self):
        
        max_coin = max(self.portfolio_analysis, key=lambda x : x["비중"])
        max_coin_name = max_coin["코인"]
        
        return max_coin_name.split("-")[1]
    

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
                    
        return profit_rate