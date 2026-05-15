from data_manager import DataManager
from pyupbit_api import PyUpbitApi
from analyzer_upbit import AnalyzerUpbit
portpolio = {
    "ticker" : "KRW-BTC",
    "period" : 365,
    "money" : 1000000,
    "fee" : 0.05
}

data_manager = DataManager()
days_candle_data_db = data_manager.load_from_database()
days_candle_data_filter = data_manager.dict_from_dataframe(days_candle_data_db)
days_candle_data = {
    "KRW-BTC" : days_candle_data_filter["KRW-BTC"]
}

pyupbit_api = PyUpbitApi(portpolio["ticker"], portpolio["period"])
current_price = pyupbit_api.get_current_price()

analyzer_upbit = AnalyzerUpbit(current_price, days_candle_data)
ma5 = analyzer_upbit.get_ma(5)
ma20 = analyzer_upbit.get_ma(20)

data_manager.add_columns(days_candle_data, "ma5", ma5)
data_manager.add_columns(days_candle_data, "ma20", ma20)

print(f"데이터 :{analyzer_upbit.get_back_test()}")