import requests
from datetime import datetime
import time
import json

import requests

def get_historical_close_api(ticker, days_ago):
    url = "https://api.upbit.com/v1/candles/days"

    params = {
        "market": ticker,
        "count": days_ago
    }

    response = requests.get(url, params=params)
    candle_data = response.json()
    
    current_price = candle_data[0]["trade_price"]
    past_price = candle_data[-1]["trade_price"]

    return {
        "current_price": current_price, 
        "past_price": past_price
        }

#비교할 암호화폐 목록(리스트)
tickers = ["KRW-BTC", "KRW-ETH", "KRW-XRP", "KRW-SOL"]
days_ago = 30

current_past = {}
#호출 함수에서 ticker가 str타입으로 받아야해서 for문 돌림
for item in tickers:
    price = get_historical_close_api(item, days_ago)
    current_past[item] = price

result = []
#중복딕셔너리 분리
for ticker, price in current_past.items():
    current = price["current_price"]
    past = price["past_price"]
    
    #print(f"종목 : {ticker}, 현재가격 : {current}, 과거가격 : {past}")
    
    #수익률 계산
    return_rate = ((current - past) / past) * 100
     
    #print(f"수익률{return_rate}")
    ticker_name = ticker.split("-")[1]
    result.append({
        "ticker" : ticker_name,
        "수익률" : return_rate
    })
      
#print(f"결과{result}") 


result.sort(key=lambda x: x["수익률"], reverse=True)

print(f"{"코인"} {"수익률":>21}")
print("=" * 30)
for item in result:
    print(f"{item["ticker"]} {item["수익률"]:>20.2f}%")
    
first = result[0]
last = result[-1]
print("\n")
print("=" * 30)
print(f"가장 많이 상승한 코인 : {first["ticker"]:>10}")
print(f"가장 많이 하락한 코인 : {last["ticker"]:>10}")
print("=" * 30)