from pyupbit_api import PyUpbitApi
from analyzer_upbit import AnalyzerUpbit
from data_manager import DataManager
from util_func import print_data_pipeline
from graph import graph_pipeline

def api_data(tickers, days):
    pyupbit_api = PyUpbitApi(tickers, days)

    ticker_lists = pyupbit_api.get_ticker_lists()
    current_prices = pyupbit_api.get_current_price()
    days_candle_data = pyupbit_api.get_candle_data()

    return ticker_lists, current_prices, days_candle_data


def save_data(data_manager, days_candle_data):
    db_df = data_manager.dataframe_from_dict(days_candle_data)
    data_manager.save_to_database(db_df)
    sql_db_frame = data_manager.load_from_database()
    filter_sql_db_frame = data_manager.filter_days(sql_db_frame, 60)
    
    filter_sql_db_frame = filter_sql_db_frame.dropna()
    return filter_sql_db_frame


def add_analysis_columns(data_manager, current_prices, days_candle_data):
    analyzer_upbit = AnalyzerUpbit(current_prices, days_candle_data)

    data_manager.add_columns(days_candle_data, "current_prices", current_prices)

    return_rate_one = analyzer_upbit.get_return_rate_d(1)
    return_rate_seven = analyzer_upbit.get_return_rate_d(7)
    return_rate_thirty = analyzer_upbit.get_return_rate_d(30)

    data_manager.add_columns(days_candle_data, "return_rate_one", return_rate_one)
    data_manager.add_columns(days_candle_data, "return_rate_seven", return_rate_seven)
    data_manager.add_columns(days_candle_data, "return_rate_thirty", return_rate_thirty)

    ma5 = analyzer_upbit.get_ma(5)
    ma20 = analyzer_upbit.get_ma(20)
    ma60 = analyzer_upbit.get_ma(60)

    data_manager.add_columns(days_candle_data, "ma5", ma5)
    data_manager.add_columns(days_candle_data, "ma20", ma20)
    data_manager.add_columns(days_candle_data, "ma60", ma60)

    volatility_n, std = analyzer_upbit.get_volatility(20)
    upper_band = analyzer_upbit.get_upper_band(ma20, std)
    lower_band = analyzer_upbit.get_lower_band(ma20, std)

    data_manager.add_columns(days_candle_data, "volatility_n", volatility_n)
    data_manager.add_columns(days_candle_data, "upper_band", upper_band)
    data_manager.add_columns(days_candle_data, "lower_band", lower_band)

    return days_candle_data


def result_data(days_candle_data):
    print_data_pipeline(days_candle_data)
    graph_pipeline(days_candle_data)


def p_one_data_pipeline():
    tickers = ["KRW-BTC", "KRW-ETH", "KRW-SOL", "KRW-XRP"]
    days = 180

    ticker_lists, current_prices, days_candle_data = api_data(tickers, days)

    data_manager = DataManager()
    
    sql_db_frame = save_data(data_manager, days_candle_data)
    days_candle_data = data_manager.dict_from_dataframe(sql_db_frame)

    days_candle_data = add_analysis_columns(
        data_manager,
        current_prices,
        days_candle_data
    )

    result_data(days_candle_data)

    return sql_db_frame