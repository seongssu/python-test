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
from Print_Message import Print_Message
       
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

portfolio_analysis = analyzer.analyze_portfolio()
#analyzer.print_message()
max_coin_name = analyzer.get_max_coin()

profit_rate = analyzer.get_profit_max_coin(price_past_today)

print_message = Print_Message(portfolio_analysis, max_coin_name, profit_rate)

print_message.print_message()

candle_data = upbit.get_candle_data_api()
graph = Graph(candle_data)
graph.get_graph_coin_profit()
        
