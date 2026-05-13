from pyupbit_api import PyUpbitApi
from analyzer_upbit import AnalyzerUpbit
import datetime
import pandas as pd

def analysis_money(portfolio, return_rate_ninety):
    current_total_money = 0
    invest_total_money = 0
    result_portfolio = {}
    for ticker, data in portfolio.items():
        amount = data["amount"]
        weight = data["weight"]
        return_rate = return_rate_ninety[ticker]
        
        profit_money = (amount * return_rate) /100
        profit_total_money = amount + profit_money
        
        invest_total_money += amount
        current_total_money += profit_total_money
        
        result_portfolio[ticker] = {
            "portfolio_weight" : weight * 100,
            "invest_money" : amount,
            "return_rate" : return_rate,
            "profit_money" : profit_money,
            "profit_total_money" : profit_total_money
        }
    for ticker, data in result_portfolio.items():
        data["current_weight"] = (data["profit_total_money"] / current_total_money) * 100   
    
    total_profit = ((current_total_money/invest_total_money) - 1) * 100
    return result_portfolio, invest_total_money, current_total_money, total_profit

def print_portfolio(result_portfolio, invest_total_money, current_total_money, total_profit, mdd):
    days = 90
    date_today = datetime.date.today()
    date_start = date_today - datetime.timedelta(days= days)
    print("=== 포트폴리오 성과 요약 ===")
    print(f"투자 기간 {":":>5} {date_start} ~ {date_today} ({days}일)" )
    print(f"초기 자산 {":":>5} {invest_total_money:,.0f} 원")
    print(f"현재 자산 {":":>5} {current_total_money:,.0f} 원")
    print(f"총 수익률 {":":>5} {total_profit:+.2f}%")
    print(f"MDD {":":>11} {mdd:+.2f}%\n")
    print(f"종목별 기여도:")
    for ticker, data in result_portfolio.items():
        print(f"{ticker:>10} {"수익률":>5} {data["return_rate"]:>+7.2f}% {"기여":>5} {data["current_weight"]:+7.2f}%")
# 90일 전에 구매한 코인 종목들의 최대낙폭(mdd) 계산
def get_mdd(portfolio, days_candle_data):
    days_portfolio_prices = None
    
    for ticker, data in portfolio.items():
        amount = data["amount"]
        df = days_candle_data[ticker]
        
        close_price = df["close"].iloc[0]
        buy_coin_count = amount / close_price
        
        days_my_coin_prices = df["close"] * buy_coin_count
        
        if days_portfolio_prices is None:
            days_portfolio_prices = days_my_coin_prices
        else:
            days_portfolio_prices += days_my_coin_prices
    days_max_coin_prices = days_portfolio_prices.cummax()
    drop_from_max = ((days_portfolio_prices - days_max_coin_prices)) / days_max_coin_prices
    mdd = drop_from_max.min() * 100
    
    return mdd
    
portfolio = {
    'KRW-BTC' : {'weight' : 0.4, 'amount' : 4_000_000},
    'KRW-ETH' : {'weight' : 0.3, 'amount' : 3_000_000},
    'KRW-SOL' : {'weight' : 0.2, 'amount' : 2_000_000},
    'KRW-XRP' : {'weight' : 0.1, 'amount' : 1_000_000}
}
fee_rate = 0.0005
invest_day_ago = 90
money_invest = 10000000

category = "portfolio"
pyupbit_api = PyUpbitApi(list(portfolio.keys()), invest_day_ago, category)

current_prices = pyupbit_api.get_current_price()
days_candle_data = pyupbit_api.get_candle_data()

analyzerupbit = AnalyzerUpbit(current_prices, days_candle_data)

return_rate_ninety = analyzerupbit.get_return_rate_d(invest_day_ago)
result_portfolio, invest_total_money, current_total_money, total_profit = analysis_money(portfolio, return_rate_ninety)

mdd = get_mdd(portfolio, days_candle_data)

print_portfolio(result_portfolio, invest_total_money, current_total_money, total_profit, mdd)

