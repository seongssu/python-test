from pyupbit_api import PyUpbitApi
from analyzer_upbit import AnalyzerUpbit
from util_func import print_portfolio
from data_manager import DataManager
from graph import graph_portfolio

portfolio = {
    'KRW-BTC' : {'weight' : 0.4, 'amount' : 4_000_000},
    'KRW-ETH' : {'weight' : 0.3, 'amount' : 3_000_000},
    'KRW-SOL' : {'weight' : 0.2, 'amount' : 2_000_000},
    'KRW-XRP' : {'weight' : 0.1, 'amount' : 1_000_000}
}
fee_rate = 0.0005
invest_day_ago = 90
money_invest = 10000000

pyupbit_api = PyUpbitApi(list(portfolio.keys()), invest_day_ago)

current_prices = pyupbit_api.get_current_price()
days_candle_data = pyupbit_api.get_candle_data()

analyzerupbit = AnalyzerUpbit(current_prices, days_candle_data)

return_rate_ninety = analyzerupbit.get_return_rate_d(invest_day_ago)
result_portfolio, invest_total_money, current_total_money, total_profit = analyzerupbit.get_portfolio_values(portfolio, return_rate_ninety)

mdd, days_portfolio_prices = analyzerupbit.get_mdd(portfolio)

print_portfolio(result_portfolio, invest_total_money, current_total_money, total_profit, mdd)

datamanager = DataManager(days_candle_data)

db_days_candle_data = datamanager.to_dataframe(days_candle_data)

filter_db = db_days_candle_data[["ticker", "close","portfolio_value"]]

graph_portfolio(days_candle_data, days_portfolio_prices)
