
from analyzer_upbit import AnalyzerUpbit
from show_project.print_project import print_portfolio
from db_manager.data_manager import DataManager
from show_project.graph import graph_portfolio
from show_project.heat_map import heat_map_portfolio

def load_candle_data(data_manager, days_ago):
    df = data_manager.load_from_database("one_result_multi_data")
    current_data = data_manager.load_from_database("one_result_single_data")
    filter_df = data_manager.filter_days(df, days_ago)
    filter_current_data = data_manager.dict_from_dataframe(current_data)    

    return data_manager.dicts_from_dataframe(filter_df), filter_current_data

def analyze_portfolio(portfolio, days_ago):
    data_manager = DataManager()
    days_candle_data, filter_current_data = load_candle_data(data_manager, days_ago)

    current_prices = {ticker: data["current_prices"]for ticker, data in filter_current_data.items()}
    analyzer = AnalyzerUpbit(days_candle_data)

    return_rate = analyzer.get_return_rate_d(current_prices, days_ago)
    profit_days_by_ticker = analyzer.get_profit_days()
    data_manager.add_columns(days_candle_data, "profit_days_by_ticker", profit_days_by_ticker)
    db_days_candle_data = data_manager.dataframe_from_dicts(days_candle_data)
    data_manager.save_to_database(db_days_candle_data, "two_result_multi_data")

    result_portfolio, invest_total_money, current_total_money, total_profit = (
        analyzer.get_portfolio_values(portfolio, return_rate)
    )

    mdd, days_portfolio_prices = analyzer.get_mdd(portfolio) 
    
    for ticker, data in result_portfolio.items():
        filter_current_data[ticker].update(data)
    db_filter_current_data = data_manager.dataframe_from_dict(filter_current_data)
    data_manager.save_to_database(db_filter_current_data, "two_result_single_data")     
    
    result_single = {
    "result_single_portfolio":{
    "invest_total_money": invest_total_money,
    "current_total_money": current_total_money,
    "total_profit": total_profit,
    "mdd": float(mdd)}}   
    df_result_single = data_manager.dataframe_from_dict(result_single)
    data_manager.save_to_database(df_result_single, "two_result_total_single_data")
    
    days_portfolio_df = days_portfolio_prices.rename("days_portfolio_prices").reset_index()
    data_manager.save_to_database(days_portfolio_df, "two_daily_portfolio_data")
    return result_portfolio, days_candle_data, result_single, days_portfolio_prices, profit_days_by_ticker

def p_two_portfolio():
    
    portfolio = {
        'KRW-BTC': {'weight': 0.4, 'have_money': 4_000_000},
        'KRW-ETH': {'weight': 0.3, 'have_money': 3_000_000},
        'KRW-SOL': {'weight': 0.2, 'have_money': 2_000_000},
        'KRW-XRP': {'weight': 0.1, 'have_money': 1_000_000},
    }

    days_ago = 90

    result_portfolio, days_candle_data, result_single, days_portfolio_prices, profit_days_by_ticker = analyze_portfolio(
        portfolio=portfolio,
        days_ago = days_ago
    )

    print_portfolio(
        result_portfolio,
        result_single
    )

    graph_portfolio(
        days_candle_data,
        days_portfolio_prices
    )
    
    heat_map_portfolio(
        profit_days_by_ticker
    )