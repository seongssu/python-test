import requests
from datetime import datetime
import time
import json
# 2. 현재가 조회 함수 작성 (get_current_prices_api)
def get_current_prices_api(tickers):

    url = "https://api.upbit.com/v1/ticker"
    headers = {"accept": "application/json"}    
    markets_param = ",".join(tickers)
    params = {"markets": markets_param}
    response = requests.get(url, headers=headers, params=params)
    prices_data = response.json()
    prices = {}
    for data in prices_data:
        prices[data['market']] = data['trade_price']

    return prices   
# 현재가 prices로 쓰니 다음부터 동일하게 쓰겠음.


# 3. 포트폴리오 분석 함수 작성 (analyze_portfolio)
def analyze_portfolio(portfolio):
    tickers = list(portfolio.keys())
    get_current_prices_api(tickers)



# 1. 포트폴리오 정의
portfolio = {
    "KRW-BTC": 0.1,
    "KRW-ETH": 3,
    "KRW-XRP": 1000
}
analyze_portfolio(portfolio)