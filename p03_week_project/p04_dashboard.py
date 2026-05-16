from show_project.graph import graph_pipeline, graph_portfolio, graph_back_test
from show_project.heat_map import heat_map_portfolio
from p01_data_pipeline import p_one_data_pipeline
from p02_portfolio import p_two_portfolio
from p03_backtesting import p_three_backtesting
from dashboard.dashboard_util import get_backtest_cards, get_trade_table, get_trade_rows, get_pipeline_cards, get_charts_html, get_html, get_portfolio_cards,get_result_portfolio_card
import webbrowser


days_candle_data = p_one_data_pipeline()

(days_portfolio_prices,
 days_portfolio_mdd,
 profit_days,
 invest_total_money,
 current_total_money,
 total_profit,
 result_portfolio) = p_two_portfolio()

(condition_buy_sell, 
 trade_history, 
 backtest_mdd, 
 result_back_test, 
 becktest_portfolio) = p_three_backtesting()

fig_pipeline = graph_pipeline(days_candle_data)
fig_portfolio = graph_portfolio(days_candle_data, days_portfolio_prices)
fig_backtesting = graph_back_test(condition_buy_sell, trade_history)

pipeline_cards = get_pipeline_cards(days_candle_data)
pipeline_html = fig_pipeline.to_html(
    full_html = False,
    include_plotlyjs = "cdn"
)

portfolio_cards = get_portfolio_cards(invest_total_money,
                                      current_total_money, 
                                      total_profit, 
                                      days_portfolio_mdd)
result_portfolio_card = get_result_portfolio_card(result_portfolio)
portfolio_html = fig_portfolio.to_html(
    full_html = False,
    include_plotlyjs = False
)

trade_rows = get_trade_rows(trade_history)
trade_table = get_trade_table(trade_rows)
backtest_cards = get_backtest_cards(becktest_portfolio, 
                                    result_back_test, 
                                    backtest_mdd)
backtesting_html = fig_backtesting.to_html(
    full_html = False,
    include_plotlyjs = False
)    

heatmap_html = heat_map_portfolio(profit_days)
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