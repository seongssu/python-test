from graph import graph_pipeline, graph_portfolio, graph_back_test
from p01_data_pipeline import p_one_data_pipeline
from p02_portfolio import p_two_portfolio
from p03_backtesting import p_three_backtesting
from datetime import datetime
import webbrowser
days_candle_data = p_one_data_pipeline()
days_portfolio_prices, days_portfolio_mdd = p_two_portfolio()
condition_buy_sell, trade_history, backtest_mdd = p_three_backtesting()

fig_pipeline = graph_pipeline(days_candle_data)
fig_portfolio = graph_portfolio(days_candle_data, days_portfolio_prices)
fig_backtesting = graph_back_test(condition_buy_sell, trade_history)

pipeline_html = fig_pipeline.to_html(
    full_html = False,
    include_plotlyjs = "cdn"
)
portfolio_html = fig_portfolio.to_html(
    full_html = False,
    include_plotlyjs = False
)
backtesting_html = fig_backtesting.to_html(
    full_html = False,
    include_plotlyjs = False
)
today = datetime.now().strftime("%Y-%m-%d")

charts_html = [
    f"""
    <div class="section">
        <h2>[섹션 1] 시세 현황</h2>
        {pipeline_html}
    </div>
    """,
    f"""
    <div class="section">
        <h2>[섹션 2] 포트폴리오</h2>
        {portfolio_html}
    </div>
    """,
    f"""
    <div class="section">
        <h2>[섹션 3] 백테스팅</h2>
        {backtesting_html}
    </div>
    """
]

html = f"""
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>암호화폐 대시보드</title>
        <style>
            body {{ font-family: Arial, sans-serif; background: #f5f5f5; padding: 24px; }}
            .section {{ background: white; border-radius: 12px; padding: 24px; margin-bottom: 20px; }}
            .cards {{ display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 16px; }}
            .card {{ background: #f8f9fa; border-radius: 8px; padding: 16px 24px; text-align: center; min-width: 160px; }}
            .card-label {{ font-size: 12px; color: #888; margin-bottom: 6px; }}
            .card-value {{ font-size: 22px; font-weight: 700; }}
        </style>
    </head>
    <body>
        <h1>🪙 암호화폐 포트폴리오 대시보드</h1>
        <p style="color:#888">생성: {today}</p>
        {''.join(charts_html)}
    </body>
    </html>
    """
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(html)
    
webbrowser.open("dashboard.html")