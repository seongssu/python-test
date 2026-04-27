import requests
from datetime import datetime
import time
import json
import pandas as pd
import matplotlib.pyplot as plt
from UPbit_API import get_current_prices_api

class Analyzer_Portfolio:
    def __init__(self, portfolio):
        self.portfolio = portfolio

    def analyze_portfolio(self):

        tickers = list(self.portfolio.keys())

        prices = get_current_prices_api(tickers)

        portfolio_analysis = []
        total_value = 0

        for stocks, volumes in self.portfolio.items():

            current_price = prices.get(stocks,0)
            value = current_price * volumes

            portfolio_analysis.append({
                "코인" : stocks,
                "수량" : volumes,
                "현재가격" : current_price,
                "가치" : value
        })

            total_value += value

        for x in portfolio_analysis:
            x["비중"] = (x["가치"]/total_value) * 60

        print(f"\n\n {"코인":<10} {"수량":>5} {"현재가":>21} {"가치":>20} {"비중":>14}")
        print("-" * 100)

        ratio_coin = {}
        all_ratio = []
        #비중 = 내가보유중인 코인중의 현재 가치 비율
        for x in portfolio_analysis:
            stocks = x["코인"]
            volumes = x["수량"]
            current_price = x["현재가격"]
            value = x["가치"]
            ratio = x["비중"]

            print(f"{stocks:<10} {volumes:>10}주 {current_price:>20}원 {value:>20}원 {ratio:>15.1f}%")
            all_ratio.append(ratio)
            ratio_coin[ratio] = stocks
            
        max_ratio_coin = max(all_ratio)
        max_coin = ratio_coin[max_ratio_coin]
        
        #print(f"최대 비중인 코인 : {max_coin}")
        return max_coin