from pyupbit_api import PyUpbitApi
from analyzer_upbit import AnalyzerUpbit
from util_func import print_basic_statistics

tickers = ["KRW-BTC", "KRW-ETH", "KRW-SOL", "KRW-XRP"]
days = 180

pyupbit_api = PyUpbitApi(tickers, days)

ticker_lists = pyupbit_api.get_ticker_lists()

current_prices = pyupbit_api.get_current_price()

days_candle_data = pyupbit_api.get_candle_data()

analyzer_upbit = AnalyzerUpbit(current_prices, days_candle_data)

one_days_ago = 1
seven_days_ago = 7
thirty_days_ago = 30
return_rate_one = analyzer_upbit.get_return_rate_d(one_days_ago)
return_rate_seven = analyzer_upbit.get_return_rate_d(seven_days_ago)
return_rate_thirty = analyzer_upbit.get_return_rate_d(thirty_days_ago)

five_day = 5
twenty_day = 20
sixty = 60
ma5 = analyzer_upbit.get_ma(five_day)
ma20 = analyzer_upbit.get_ma(twenty_day)
ma60 = analyzer_upbit.get_ma(sixty)

volatility_n = analyzer_upbit.get_volatility(twenty_day)
upper_band = analyzer_upbit.get_upper_band()
lower_band = analyzer_upbit.get_lower_band()

current_day = days_candle_data[tickers[0]].index[-1].date()
print_basic_statistics(current_day, tickers, current_prices, return_rate_seven, return_rate_thirty, volatility_n)


 