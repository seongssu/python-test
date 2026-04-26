import requests
from datetime import datetime
import time
import json
import pandas as pd
import matplotlib.pyplot as plt

def get_candle_data_api(ticker, count):
    
    #url 끝에 공백이 들어가면 안된다. 잘못된 주소로 요청함
    url = "https://api.upbit.com/v1/candles/days"
    headers = {"accept": "application/json"}
    params = {
        "market" : ticker,
        "count" : count 
    }
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    
    return data

ticker = "KRW-BTC"
count = 30

data = get_candle_data_api(ticker, count)
#print(f"데이터 {data}")
prices_date = []
#순서 반대로
data = data[::-1]

for item in data:      
    date = item['candle_date_time_kst']
    prices = item['trade_price']

    #print(f"종가 : {prices}, 날짜 : {date} ")
    
    prices_date.append([date, prices])

#print(f"날짜 종가 리스트 : {prices_date}")
pd_prices_date = pd.DataFrame(prices_date)
#print(pd_prices_date)

five_data = pd_prices_date[1].rolling(5).mean()
ten_data = pd_prices_date[1].rolling(10).mean()

#print(f"5일선 : {five_data.values[-1]}")
#print(f"10일선 : {ten_data.values[-1]}")

# 종가
plt.plot(pd_prices_date[0], pd_prices_date[1], label="price")

# 5일선
plt.plot(pd_prices_date[0], five_data, label="MA5")

# 10일선
plt.plot(pd_prices_date[0], ten_data, label="MA10")

plt.show()

if five_data.values[-1] > ten_data.values[-1]:
    print("단기 상승 흐름")
elif five_data.values[-1] < ten_data.values[-1]:
    print("단기 하락 흐름")
else:
    print("변동 없음")
