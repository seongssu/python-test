from db_manager.data_manager import DataManager
from remote.pyupbit_api import PyUpbitApi
from analyzer_upbit import AnalyzerUpbit
from show_project.print_project import print_back_test, print_result_back_test
from show_project.graph import graph_back_test

def p_three_backtesting():
    portfolio = {
        "ticker" : "KRW-BTC",
        "period" : 365,
        "have_money" : 1000000,
        "fee" : 0.05
    }

    data_manager = DataManager()
    days_candle_data_db = data_manager.load_from_database()
    days_candle_data_filter = data_manager.dict_from_dataframe(days_candle_data_db)
    days_candle_data = {
        "KRW-BTC" : days_candle_data_filter["KRW-BTC"]
    }

    pyupbit_api = PyUpbitApi(portfolio['ticker'], portfolio['period'])
    current_price = pyupbit_api.get_current_price()

    analyzer_upbit = AnalyzerUpbit(current_price, days_candle_data)
    ma5 = analyzer_upbit.get_ma(5)
    ma20 = analyzer_upbit.get_ma(20)

    data_manager.add_columns(days_candle_data, "ma5", ma5)
    data_manager.add_columns(days_candle_data, "ma20", ma20)

    trade_history, result_back_test, condition_buy_sell = analyzer_upbit.get_trade_history(portfolio)
    print_back_test(trade_history)

    mdd_portfolio = {
        portfolio["ticker"]: {
            "have_money": portfolio["have_money"]
        }
    }
    mdd, days_portfolio_prices = analyzer_upbit.get_mdd(mdd_portfolio)
    print_result_back_test(portfolio, trade_history, result_back_test, mdd)
    graph_back_test(condition_buy_sell, trade_history)
    
    return condition_buy_sell, trade_history, mdd, result_back_test, portfolio