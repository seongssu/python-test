from pyupbit_api import PyUpbitApi

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
pyupbit_api = PyUpbitApi(portfolio.keys(), invest_day_ago, category)

days_candle_data = pyupbit_api.get_candle_data()

print(f"캔들데이터 : {days_candle_data}")