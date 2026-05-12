from pyupbit_api import PyUpbitApi
from analyzer_upbit import AnalyzerUpbit
from data_manager import DataManager
from util_func import print_basic_statistics
from graph import graph

tickers = ["KRW-BTC", "KRW-ETH", "KRW-SOL", "KRW-XRP"]
days = 180

pyupbit_api = PyUpbitApi(tickers, days)

ticker_lists = pyupbit_api.get_ticker_lists()

current_prices = pyupbit_api.get_current_price()

days_candle_data = pyupbit_api.get_candle_data()

analyzer_upbit = AnalyzerUpbit(current_prices, days_candle_data)
data_manager = DataManager(days_candle_data)

data_manager.add_columns("current_prices", current_prices)

one_days_ago = 1
seven_days_ago = 7
thirty_days_ago = 30
return_rate_one = analyzer_upbit.get_return_rate_d(one_days_ago)
return_rate_seven = analyzer_upbit.get_return_rate_d(seven_days_ago)
return_rate_thirty = analyzer_upbit.get_return_rate_d(thirty_days_ago)
data_manager.add_columns("return_rate_one", return_rate_one)
data_manager.add_columns("return_rate_seven", return_rate_seven)
data_manager.add_columns("return_rate_thirty", return_rate_thirty)

five_day = 5
twenty_day = 20
sixty = 60
ma5 = analyzer_upbit.get_ma(five_day)
ma20 = analyzer_upbit.get_ma(twenty_day)
ma60 = analyzer_upbit.get_ma(sixty)
data_manager.add_columns("ma5", ma5)
data_manager.add_columns("ma20", ma20)
data_manager.add_columns("ma60", ma60)

volatility_n = analyzer_upbit.get_volatility(twenty_day)
upper_band = analyzer_upbit.get_upper_band(ma20)
lower_band = analyzer_upbit.get_lower_band(ma20)
data_manager.add_columns("volatility_n", volatility_n)
data_manager.add_columns("upper_band", upper_band)
data_manager.add_columns("lower_band", lower_band)

current_day = days_candle_data[tickers[0]].index[-1].date()
print_basic_statistics(days_candle_data)

graph(days_candle_data)
#print(f"밴드: {days_candle_data}")
#print(f"칼럼 : {days_candle_data[tickers[0]].columns}")