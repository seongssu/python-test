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

# 2. 현재가 조회 함수
       
portfolio = {
    "KRW-BTC":0.1,
    "KRW-ETH":3,
    "KRW-XRP":1000
}
ticker = []
ticker = [item for item in portfolio]
days_ago = 7

upbit = UPbit(ticker, days_ago)
prices = upbit.get_current_prices_api()
analyzer = Analyzer_Portfolio(portfolio, prices)
max_coin = analyzer.analyze_portfolio()
price_past_today = upbit.get_historical_close_api()
analyzer.get_profit_max_coin(price_past_today)

print(f"보유 비중 상위 1개 코인 : {max_coin}")
# def get_graph_coin_profit(self):

#         coin_price_change = self.get_candle_data_api()[::-1]
#         coin_price = []
#         coin_date = []

#         for item in coin_price_change:
#             date = item["candle_date_time_kst"]
#             price = item["trade_price"]
#             split_date = date.split("T")[0]
#             slice_date = split_date[2:]
            
#             coin_price.append(price)
#             coin_date.append(slice_date)

#         #print(f"날짜가격 : {coin_date}")
#         plt.plot(coin_date,coin_price, label="MA7")
#         plt.show()
        
