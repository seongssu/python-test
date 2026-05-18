from remote.pyupbit_api import PyUpbitApi
from analyzer_upbit import AnalyzerUpbit
from db_manager.data_manager import DataManager
from show_project.print_project import print_data_pipeline
from show_project.graph import graph_pipeline

def api_data(tickers, days, table_name):
    pyupbit_api = PyUpbitApi(tickers, days)

    ticker_lists = pyupbit_api.get_ticker_lists()
    current_prices = pyupbit_api.get_current_price()
    days_candle_data = pyupbit_api.get_candle_data(table_name)

    return ticker_lists, current_prices, days_candle_data


def save_candle_data(data_manager, days_candle_data):
    db_df = data_manager.dataframe_from_dicts(days_candle_data)
    data_manager.save_to_database(db_df, "candle_api_data")
    candle_df = data_manager.load_from_database("candle_api_data")
    filter_candle_df = data_manager.filter_days(candle_df, 60)
    return filter_candle_df

def save_current_result_data(data_manager, current_summary):
    df_current_prices = data_manager.dataframe_from_dict(current_summary)
    data_manager.save_to_database(df_current_prices, "result_current_data")


def add_analysis_columns(data_manager, current_prices, days_candle_data):
    analyzer_upbit = AnalyzerUpbit(days_candle_data)
    
    return_rate_one = analyzer_upbit.get_return_rate_d(current_prices, 1)
    return_rate_seven = analyzer_upbit.get_return_rate_d(current_prices, 7)
    return_rate_thirty = analyzer_upbit.get_return_rate_d(current_prices, 30)
    volatility_n, std = analyzer_upbit.get_volatility(20)
    
    ma5 = analyzer_upbit.get_ma(5)
    ma20 = analyzer_upbit.get_ma(20)
    ma60 = analyzer_upbit.get_ma(60)
    
    upper_band = analyzer_upbit.get_upper_band(ma20, std)
    lower_band = analyzer_upbit.get_lower_band(ma20, std)
    
    data_manager.add_columns(days_candle_data, "ma5", ma5)
    data_manager.add_columns(days_candle_data, "ma20", ma20)
    data_manager.add_columns(days_candle_data, "ma60", ma60)
    data_manager.add_columns(days_candle_data, "upper_band", upper_band)
    data_manager.add_columns(days_candle_data, "lower_band", lower_band)  

    conversion_current_data = data_manager.conversion_from_current_prices(current_prices, "current_prices")
    data_manager.add_columns(conversion_current_data, "return_rate_one", return_rate_one)
    data_manager.add_columns(conversion_current_data, "return_rate_seven", return_rate_seven)
    data_manager.add_columns(conversion_current_data, "return_rate_thirty", return_rate_thirty)
    data_manager.add_columns(conversion_current_data, "volatility_n", volatility_n)
    
    return days_candle_data, conversion_current_data


def result_data(days_candle_data, current_summary):
    print_data_pipeline(current_summary)
    graph_pipeline(days_candle_data, current_summary)


def p_one_data_pipeline():
    tickers = ["KRW-BTC", "KRW-ETH", "KRW-SOL", "KRW-XRP"]
    days = 365

    _, current_prices, days_candle_data = api_data(tickers, days, table_name = "candle_api_data")

    data_manager = DataManager()
    
    candle_df = save_candle_data(data_manager, days_candle_data)
    days_candle_data = data_manager.dicts_from_dataframe(candle_df)

    days_candle_data, current_summary = add_analysis_columns(
        data_manager,
        current_prices,
        days_candle_data
    )

    result_data(days_candle_data, current_summary)    
    
    save_current_result_data(data_manager, current_summary)