import requests
from datetime import datetime
import time
import json

def get_single_price_api(ticker):
    url = "https://api.upbit.com/v1/ticker"
    headers = {"accept": "application/json"}

    params = {"markets": ticker}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()[0]
    return data['trade_price']

def price_alert_system(ticker, high_target, low_target):
    print(f"{"코인명":<10} {"상한가목표값":>20} {"하한가목표값":>20}")
    print("=" * 80)
    print(f"{ticker:<10} {high_target:>28.0f}원 {low_target:>23.0f}원 \n\n" )
    print(f"{"조회시간"} {"현재가격":>25}" )
    print("-" * 80)
    for num in range(1,20):
        current_price = get_single_price_api(ticker)
        current_time = datetime.now().strftime("%H%M%S")
        print(f"{current_time} {current_price:>30,.0f}원 ")
        
        if current_price >= high_target:
            print("상한가 도달")
        elif current_price <= low_target:
            print("하한가 도달")
        else: 
            print("정상 범위")
        
        

ticker = "KRW-BTC"
#현재 가격
current_price = get_single_price_api(ticker)
#현재가를 기준으로 상한가와 하한가를 계산합니다.
high_target = current_price * 1.05
low_target = current_price * 0.95

price_alert_system(ticker, high_target, low_target)

