from PyUpbit_API import PyUpbit_Api

tickers = ["KRW-BTC", "KRW-ETH", "KRW-SOL", "KRW-XRP"]
days = 180

pyupbit_api = PyUpbit_Api(tickers, days)

ticker_lists = pyupbit_api.get_ticker_lists()

current_prices = pyupbit_api.get_current_price()

days_candle_data = pyupbit_api.get_candle_data()

print(f"타입 : {type(days_candle_data)}")
# for market in tickers_list:
#     print(f"py 마켓 : {type(market)}")