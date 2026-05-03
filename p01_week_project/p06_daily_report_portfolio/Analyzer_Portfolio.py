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
        max_coin_name = self.get_max_coin()
        
        return max_coin_name
    
    def get_max_coin(self):
        
        max_coin = max(self.portfolio_analysis, key=lambda x : x["비중"])
        max_coin_name = max_coin["코인"]
        
        return max_coin_name.split("-")[1]
    
    def print_message(self):
        
        print(f"\n\n {"코인":<10} {"수량":>5} {"현재가":>21} {"가치":>20} {"비중":>14}")
        print("-" * 100)
        
        for x in self.portfolio_analysis:
            stocks = x["코인"]
            volumes = x["수량"]
            current_price = x["현재가격"]
            value = x["가치"]
            ratio = x["비중"]
            stocks_name = stocks.split("-")[1]
            print(f"{stocks_name:<10} {volumes:>10}{stocks_name} {current_price:>20,.0f}원 {value:>20,.0f}원 {ratio:>15.1f}%")
    
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
        print(f"\n최고수익코인 : {coin_profit["ticker"]}")       
        
        return profit_rate