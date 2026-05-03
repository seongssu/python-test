import requests
from datetime import datetime
import time
import json
import pandas as pd
import matplotlib.pyplot as plt
from Analyzer_Portfolio import Analyzer_Portfolio
#from UPbit_API import get_historical_close_api
#from UPbit_API import get_candle_data_api
from UPbit_API import UPbit

# 2. 현재가 조회 함수
       
portfolio = {
    "KRW-BTC":0.1,
    "KRW-ETH":3,
    "KRW-XRP":1000
}
#1 오늘 기준 총 포트폴리오 가치
#2 보유 비중 상위1개 코인
analyzer = Analyzer_Portfolio(portfolio)
max_coin = analyzer.analyze_portfolio()
print(f"보유 비중 상위 1개 코인 : {max_coin}")

#3 최근 7일 기준 가장 많이 오른 코인
ticker = []
#최근 7일중 가장 많이 오른 보유 코인
ticker = [item for item in portfolio]
days_ago = 7

upbit = UPbit(ticker, days_ago)

price_past_today = upbit.get_historical_close_api()
#print(f"N일전과 현재 가격 : {price_past_today}")

profit_rate = []
for ticker, price in price_past_today.items():
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

coin_price_change = upbit.get_candle_data_api()

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