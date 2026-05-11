from PyUpbit_API import PyUpbit_Api
from Analyzer_Upbit import Analyzer_Upbit

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

five_day = 5
twenty_day = 20
sixty = 60
ma5 = analyzer_upbit.get_ma(five_day)
ma20 = analyzer_upbit.get_ma(twenty_day)
ma60 = analyzer_upbit.get_ma(sixty)

volatility_n = analyzer_upbit.get_volatility(twenty_day)
upper_band = analyzer_upbit.get_upper_band()
lower_band = analyzer_upbit.get_lower_band()

print(f"upper : {upper_band}")
print(f"lower : {lower_band}")
    