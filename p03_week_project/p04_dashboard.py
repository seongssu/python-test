from show_project.graph import graph_pipeline, graph_portfolio, graph_back_test
from show_project.heat_map import heat_map_portfolio
from db_manager.data_manager import DataManager
from dashboard.dashboard_util import get_backtest_cards, get_trade_table, get_trade_rows, get_pipeline_cards, get_charts_html, get_html, get_portfolio_cards,get_result_portfolio_card
import webbrowser
import pandas as pd

def p_four_backtesting():
    
    data_manager = DataManager()
    
    one_result_single_data_df = data_manager.load_from_database("one_result_single_data")
    two_days_candle_data_df = data_manager.load_from_database("two_result_multi_data")
    three_days_candle_data_df = data_manager.load_from_database("three_result_multi_data")    
    days_portfolio_prices_df = data_manager.load_from_database("two_daily_portfolio_data")
    two_result_total_single_data_df = data_manager.load_from_database("two_result_total_single_data")
    two_result_single_data_df = data_manager.load_from_database("two_result_single_data")
    trade_history_df = data_manager.load_from_database("three_trade_history_data")
    three_result_single_data_df = data_manager.load_from_database("three_result_single_data")
    
    
    one_result_single_data = data_manager.dict_from_dataframe(one_result_single_data_df)
    two_days_candle_data = data_manager.dicts_from_dataframe(two_days_candle_data_df)
    three_days_candle_data = data_manager.dicts_from_dataframe(two_days_candle_data_df)
    days_portfolio_prices = (days_portfolio_prices_df.set_index("date")["days_portfolio_prices"])    
    trade_history = data_manager.dict_from_dataframe(trade_history_df)
    condition_buy_sell = (three_days_candle_data_df.set_index("date"))
    one_current_data = {ticker: group.drop(columns=["ticker"])for ticker, group in one_result_single_data_df.groupby("ticker")}
    two_result_total_single_data = data_manager.dict_from_dataframe(two_result_total_single_data_df)
    two_result_single_data = data_manager.dict_from_dataframe(two_result_single_data_df)
    three_result_single_data = data_manager.dict_from_dataframe(three_result_single_data_df)
    
    fig_pipeline = graph_pipeline(three_days_candle_data, one_result_single_data)
    fig_portfolio = graph_portfolio(two_days_candle_data, days_portfolio_prices)
    fig_backtesting = graph_back_test(condition_buy_sell, trade_history)

    pipeline_cards = get_pipeline_cards(one_current_data)
    pipeline_html = fig_pipeline.to_html(
        full_html = False,
        include_plotlyjs = "cdn"
    )
    
    portfolio_cards = get_portfolio_cards(two_result_total_single_data['result_single_portfolio'])
    result_portfolio_card = get_result_portfolio_card(two_result_single_data)
    portfolio_html = fig_portfolio.to_html(
        full_html = False,
        include_plotlyjs = False
    )

    for _, data in trade_history.items():
        data["date"] = pd.to_datetime(data["date"])
    trade_rows = get_trade_rows(trade_history)
    
    trade_table = get_trade_table(trade_rows)
    backtest_cards = get_backtest_cards(three_result_single_data['result_single_back_test'])
    backtesting_html = fig_backtesting.to_html(
        full_html = False,
        include_plotlyjs = False
    )    

    heatmap_data = {
    ticker: df["profit_days_by_ticker"]
    for ticker, df in two_days_candle_data.items()
    }
    heatmap_html = heat_map_portfolio(heatmap_data)
    charts_html = get_charts_html(pipeline_cards, 
                                pipeline_html, 
                                portfolio_cards,
                                result_portfolio_card,
                                portfolio_html, 
                                backtest_cards, 
                                backtesting_html, 
                                trade_table, 
                                heatmap_html)
    html = get_html(charts_html)
        
    webbrowser.open("dashboard.html")