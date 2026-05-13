from pyupbit_api import PyUpbitApi
from analyzer_upbit import AnalyzerUpbit

def analysis_money(portfolio, return_rate_ninety):
    current_total_money = 0
    invest_total_money = 0
    result_portfolio = {}
    for ticker, data in portfolio.items():
        amount = data["amount"]
        weight = data["weight"]
        return_rate = return_rate_ninety[ticker]
        
        profit = (amount * return_rate) /100
        profit_money = amount + profit
        
        invest_total_money += amount
        current_total_money += profit_money
        
        result_portfolio[ticker] = {
            "portfolio_weight" : weight * 100,
            "invest_money" : amount,
            "return_rate" : return_rate,
            "profit" : profit,
            "profit_money" : profit_money
        }
    for ticker, data in result_portfolio.items():
        data["current_weight"] = (data["profit_money"] / current_total_money) * 100   
    
    total_profit = ((current_total_money/invest_total_money) - 1) * 100
    return result_portfolio, invest_total_money, current_total_money, total_profit

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
result_portfolio, invest_total_money, current_money, total_profit = analysis_money(portfolio, return_rate_ninety)

