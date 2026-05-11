from PyUpbit_API import PyUpbit_Api
from Analyzer_Upbit import Analyzer_Upbit
import pandas as pd

tickers = ["KRW-BTC", "KRW-ETH", "KRW-SOL", "KRW-XRP"]
days = 180

pyupbit_api = PyUpbit_Api(tickers, days)

ticker_lists = pyupbit_api.get_ticker_lists()

current_prices = pyupbit_api.get_current_price()

days_candle_data = pyupbit_api.get_candle_data()

analyzer_upbit = Analyzer_Upbit(current_prices, days_candle_data)

one_days_ago = 1
seven_days_ago = 7
analyzer_upbit.get_return_rate_d(one_days_ago)
analyzer_upbit.get_return_rate_d(seven_days_ago)