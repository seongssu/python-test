import requests
from datetime import datetime
import time
import json

def get_historical_data_api(ticker, days_count):
    url = "https://api.upbit.com/v1/candles/days"

    params = {
        "market": ticker,
        "count": days_count
    }

    response = requests.get(url, params=params)
    candle_data = response.json()

    prices = []

    for data in candle_data:
        prices.append(data["trade_price"])

    return prices

def get_single_price_api(ticker):
    url = "https://api.upbit.com/v1/ticker"

    params = {
        "markets": ticker
    }

    response = requests.get(url, params=params)

    data = response.json()[0]
    return data['trade_price']

def calculate_investment_return(money_invest, ticker, day_invest):
    #과거투자시점 가격 목록
    money_past = get_historical_data_api(ticker, day_invest)
    #나의 투자시점 구매수량
    volumes = money_invest / money_past[-1]
    #현재 가치 계산
    current_value = volumes * money_past[0]    
    
    #손익 및 수익률 계산
    #손익
    profit_loss = current_value - money_invest
    #수익률
    rate_profit = (profit_loss / money_invest) * 100
    
    print(f"{"투자일자"}        : {day_invest}일전")
    print(f"{"투자금액"}        : {money_invest:,}원")
    print(f"{"투자시점가격"}    : {money_past[-1]:,.0f}원")
    print(f"{"구매수량"}        : {volumes:.5f}BTC")
    print(f"{"현재가격"}        : {current_value:,.0f}원  ")
    print(f"{"손익"}            : {profit_loss:,.0f}원")
    print(f"{"수익률"}          : {rate_profit:.2f}%")
    
    
ticker = "KRW-BTC"
day_invest = 30
money_invest = 1000000

calculate_investment_return(money_invest, ticker, day_invest)