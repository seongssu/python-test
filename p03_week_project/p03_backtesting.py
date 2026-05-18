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
    days_candle_data_db = data_manager.load_from_database("one_result_multi_data")
    days_candle_data_filter = data_manager.dicts_from_dataframe(days_candle_data_db)    
    
    analyzer_upbit = AnalyzerUpbit(days_candle_data_filter)
    condition_buy_sell = analyzer_upbit.get_back_test()
    trade_history, result_back_test, condition_buy_sell = analyzer_upbit.get_trade_history(condition_buy_sell, portfolio)
    print_back_test(trade_history)

    mdd_portfolio = {
        portfolio["ticker"]: {
            "have_money": portfolio["have_money"]
        }
    }
    mdd, _ = analyzer_upbit.get_mdd(mdd_portfolio)
    print_result_back_test(portfolio, trade_history, result_back_test, mdd)
    graph_back_test(condition_buy_sell, trade_history)  
