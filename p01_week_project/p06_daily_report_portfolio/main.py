import requests
from datetime import datetime
import time
import json
import pandas as pd
import matplotlib.pyplot as plt
from Analyzer_Portfolio import Analyzer_Portfolio
#from UPbit_API import get_historical_close_api
#from UPbit_API import get_candle_data_api
from UPbit import UPbit
from Graph import Graph

# 2. 현재가 조회 함수
       
portfolio = {
    "KRW-BTC":0.1,
    "KRW-ETH":3,
    "KRW-XRP":1000
}

ticker = [item for item in portfolio]
days_ago = 7

upbit = UPbit(ticker, days_ago)

prices = upbit.get_current_prices_api()
price_past_today = upbit.get_historical_close_api()

analyzer = Analyzer_Portfolio(portfolio, prices)

max_coin = analyzer.analyze_portfolio()
analyzer.get_profit_max_coin(price_past_today)

print(f"보유 비중 상위 1개 코인 : {max_coin}")


candle_data = upbit.get_candle_data_api()
graph = Graph(candle_data)
graph.get_graph_coin_profit()
        
