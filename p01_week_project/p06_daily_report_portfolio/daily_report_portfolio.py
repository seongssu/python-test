import requests
from datetime import datetime
import time
import json
import pandas as pd
import matplotlib.pyplot as plt


# 2. 현재가 조회 함수
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

def analyze_portfolio(portfolio):

    tickers = list(portfolio.keys())

    prices = get_current_prices_api(tickers)

    portfolio_analysis = []
    total_value = 0

    for stocks, volumes in portfolio.items():

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
        x["비중"] = (x["가치"]/total_value) * 100

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

def get_historical_close_api(portfolio, days_ago):
    url = "https://api.upbit.com/v1/candles/days"

    result = {}
    for ticker in portfolio:
        params = {
            "market": ticker,
            "count": days_ago
        }

        response = requests.get(url, params=params)
        candle_data = response.json()
    
        current_price = candle_data[0]["trade_price"]
        past_price = candle_data[-1]["trade_price"]
        
        result[ticker] = {
            "current_price" : current_price,
            "past_price" : past_price
        }
        

    return result

def get_candle_data_api(ticker, count):

    url = "https://api.upbit.com/v1/candles/days"
    headers = {"accept": "application/json"}
    params = {
        "market" : ticker,
        "count" : count
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    return data
       
portfolio = {
    "KRW-BTC":0.1,
    "KRW-ETH":3,
    "KRW-XRP":1000
}
#1 오늘 기준 총 포트폴리오 가치
#2 보유 비중 상위1개 코인
max_coin = analyze_portfolio(portfolio)
print(f"보유 비중 상위 1개 코인 : {max_coin}")

#3 최근 7일 기준 가장 많이 오른 코인
ticker = []
#최근 7일중 가장 많이 오른 보유 코인
ticker = [item for item in portfolio]
days_ago = 7

price_past_today = get_historical_close_api(ticker, days_ago)
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

ticker_item = "KRW-BTC"

coin_price_change = get_candle_data_api(ticker_item, days_ago)

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