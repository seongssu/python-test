import requests
from datetime import datetime
import time
import json

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
# 3. 포트폴리오 분석함수
def analyze_portfolio(portfolio):
# (1)현재가 조회

# api서버를 통해 현재값을 불러와야하므로 get_current_prices_api(tickers)함수의 tickers값이 먼저 필요함.
# 보유 코인 목록을 API에 전달하여 현재가 데이터를 가져온다.(= 파라미터가 보유 코인 목록이다.  )
# ★[portfolio.keys()]와 list(portfolio.key())는 다르다?★
    tickers = list(portfolio.keys())

#get_current_prices_api(tickers)함수의 반환값 prices
    prices = get_current_prices_api(tickers)

# (2)각 암호화폐별 분석


    portfolio_analysis = []
    total_value = 0
# 현재가 × 보유 수량 → 개별 가치 계산(내가 보유중인), portfolio의 키값은 주식종목, value는 수량이다.
    for stocks, volumes in portfolio.items():
# 보유중인 주식들 현재가격 = 현재가격 X 각각의 주식들 수량
# get(매개변수,0) = 키값에 해당하는 value값들을 가져오는데 없으면 0으로 반환

      current_price = prices.get(stocks,0)
      value = current_price * volumes
      stocks_name = stocks.split("-", 1)
# portfolio_analysis 리스트에 코인명, 수량, 현재가, 가치 저장
      portfolio_analysis.append({
        "코인" : stocks,
        "수량" : volumes,
        "현재가격" : current_price,
        "가치" : value
  })
# 동시에 total_value(총합)를 누적
      total_value += value

# (3)비중 계산
# 개별 가치 ÷ 총합 × 100 으로 각 암호화폐의 비중을 추가
# 현재가 × 보유 수량
# 예: 비트코인 0.1개 × 50,000,000원 = 5,000,000원
    for x in portfolio_analysis:
        x["비중"] = (x["가치"]/total_value) * 100
#총 포트폴리오 가치를 출력한다.
    print("=" *100)
    print(f"총 포트폴리오의 가치: {total_value:,.0f}원")
    print("=" *100)
    print(f"\n\n {"코인":<10} {"수량":>5} {"현재가":>21} {"가치":>20} {"비중":>14}")
    print("-" * 100)
    #print(f"확인:{portfolio_analysis}")
    for x in portfolio_analysis:
        stocks = x["코인"]
        volumes = x["수량"]
        current_price = x["현재가격"]
        value = x["가치"]
        ratio = x["비중"]

        print(f"{stocks:<10} {volumes:>10}주 {current_price:>20}원 {value:>20}원 {ratio:>15.1f}%")


# 1. 포트폴리오의 정의, 주어진 값
portfolio = {
    "KRW-BTC":0.1,
    "KRW-ETH":3,
    "KRW-XRP":1000
}
analyze_portfolio(portfolio)