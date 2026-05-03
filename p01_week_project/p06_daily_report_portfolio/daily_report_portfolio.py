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