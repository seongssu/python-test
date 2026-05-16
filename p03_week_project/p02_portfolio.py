from remote.pyupbit_api import PyUpbitApi
from analyzer_upbit import AnalyzerUpbit
from show_project.print_project import print_portfolio
from db_manager.data_manager import DataManager
from show_project.graph import graph_portfolio
from show_project.heat_map import heat_map_portfolio

def load_candle_data(data_manager, invest_day_ago):
    df = data_manager.load_from_database()

    filter_df = data_manager.filter_days(df, invest_day_ago)

    return data_manager.dict_from_dataframe(filter_df)

def analyze_portfolio(portfolio, invest_day_ago):
    data_manager = DataManager()
    pyupbit_api = PyUpbitApi(list(portfolio.keys()), invest_day_ago)

    current_prices = pyupbit_api.get_current_price()
    days_candle_data = load_candle_data(data_manager, invest_day_ago)

    analyzer = AnalyzerUpbit(current_prices, days_candle_data)

    return_rate = analyzer.get_return_rate_d(invest_day_ago)
    profit_days_by_ticker = analyzer.get_profit_days()

    result_portfolio, invest_total_money, current_total_money, total_profit = (
        analyzer.get_portfolio_values(portfolio, return_rate)
    )

    mdd, days_portfolio_prices = analyzer.get_mdd(portfolio)

    return {
        "result_portfolio": result_portfolio,
        "profit_days_by_ticker" : profit_days_by_ticker,
        "invest_total_money": invest_total_money,
        "current_total_money": current_total_money,
        "total_profit": total_profit,
        "mdd": mdd,
        "days_candle_data": days_candle_data,
        "days_portfolio_prices": days_portfolio_prices,
    }

def p_two_portfolio():
    
    portfolio = {
        'KRW-BTC': {'weight': 0.4, 'have_money': 4_000_000},
        'KRW-ETH': {'weight': 0.3, 'have_money': 3_000_000},
        'KRW-SOL': {'weight': 0.2, 'have_money': 2_000_000},
        'KRW-XRP': {'weight': 0.1, 'have_money': 1_000_000},
    }

    invest_day_ago = 90

    result = analyze_portfolio(
        portfolio=portfolio,
        invest_day_ago = invest_day_ago
    )

    print_portfolio(
        result["result_portfolio"],
        result["invest_total_money"],
        result["current_total_money"],
        result["total_profit"],
        result["mdd"]
    )

    graph_portfolio(
        result["days_candle_data"],
        result["days_portfolio_prices"]
    )
    
    heat_map_portfolio(
        result["profit_days_by_ticker"]
    )
    return result["days_portfolio_prices"], result["mdd"], result["profit_days_by_ticker"]