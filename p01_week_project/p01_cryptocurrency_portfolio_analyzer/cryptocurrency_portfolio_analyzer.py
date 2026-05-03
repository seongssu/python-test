import requests
from datetime import datetime
import time
import json

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
      stocks_name = stocks.split("-")[1]
      
      portfolio_analysis.append({
        "코인" : stocks_name,
        "수량" : volumes,
        "현재가격" : current_price,
        "가치" : value
  })

      total_value += value

    for x in portfolio_analysis:
        x["비중"] = (x["가치"]/total_value) * 100
#총 포트폴리오 가치를 출력한다.
    print("=" *100)
    print(f"총 포트폴리오의 가치: {total_value:,.0f}원")
    print("=" *100)
    print(f"\n\n {"코인":<10} {"수량":>5} {"현재가":>21} {"가치":>20} {"비중":>14}")
    print("-" * 100)
    
    for x in portfolio_analysis:
        stocks = x["코인"]
        volumes = x["수량"]
        current_price = x["현재가격"]
        value = x["가치"]
        ratio = x["비중"]

        print(f"{stocks:<10} {volumes:>10}BTC {current_price:>20}원 {value:>20}원 {ratio:>15.1f}%")

portfolio = {
    "KRW-BTC":0.1,
    "KRW-ETH":3,
    "KRW-XRP":1000
}
analyze_portfolio(portfolio)