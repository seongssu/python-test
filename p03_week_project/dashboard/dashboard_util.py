import datetime
def get_pipeline_cards(days_candle_data):    
    portfolio_cards = ""

    for ticker, df in days_candle_data.items():
        item = df.iloc[-1]

        portfolio_cards += f"""
        <div class="card">
            <div class="card-label">{ticker}</div>
            <div class="card-value">{item["current_prices"]:,.0f}원</div>
            <div>7일 수익률: {item["return_rate_seven"]:+.2f}%</div>
            <div>30일 수익률: {item["return_rate_thirty"]:+.2f}%</div>
            <div>연환산 변동성: {item["volatility_n"]:+.2f}%</div>
        </div>
        """
    return portfolio_cards
def get_portfolio_cards(
    invest_total_money,
    current_total_money,
    total_profit,
    mdd
):
    days = 90
    date_today = datetime.date.today()
    date_start = date_today - datetime.timedelta(days= days)
    
    return f"""
    <div class="cards">
        
        <div class="card">
            <div class="card-label">투자 기간</div>
            <div class="card-value">{date_start} ~ {date_today} ({days}일)</div>
        </div>
        <div class="card">
            <div class="card-label">초기 자산</div>
            <div class="card-value">{invest_total_money:,.0f}원</div>
        </div>

        <div class="card">
            <div class="card-label">현재 자산</div>
            <div class="card-value">{current_total_money:,.0f}원</div>
        </div>

        <div class="card">
            <div class="card-label">총 수익률</div>
            <div class="card-value">{total_profit:+.2f}%</div>
        </div>

        <div class="card">
            <div class="card-label">MDD</div>
            <div class="card-value">{mdd:+.2f}%</div>
        </div>
    </div>
    """
def get_trade_rows(trade_history):
    trade_rows = ""

    for index, data in trade_history.items():
        profit = "" if data["profit_have_buy"] == "" else f'{data["profit_have_buy"]:+.2f}%'

        trade_rows += f"""
        <tr>
            <td>{index}</td>
            <td>{data["state"]}</td>
            <td>{data["date"].strftime("%Y-%m-%d")}</td>
            <td>{data["close"]:,.0f}원</td>
            <td>{data["coin_count"]:.5f}BTC</td>
            <td>{data["trade_money"]:,.0f}원</td>
            <td>{profit}</td>
        </tr>
        """
    return trade_rows 
    
def get_trade_table(trade_rows):
    trade_table = f"""
    <table>
        <tr>
            <th>#</th>
            <th>유형</th>
            <th>날짜</th>
            <th>단가</th>
            <th>수량</th>
            <th>금액</th>
            <th>수익률</th>
        </tr>
        {trade_rows}
    </table>
    """
    return trade_table

def get_backtest_cards(becktest_portfolio, result_back_test, backtest_mdd):
    backtest_cards = f"""
    <div class="cards">
        <div class="card">
            <div class="card-label">기간</div>
            <div class="card-value">{becktest_portfolio["period"]}일</div>
        </div>
        <div class="card">
            <div class="card-label">초기 자본</div>
            <div class="card-value">{becktest_portfolio["have_money"]:,.0f}원</div>
        </div>
        <div class="card">
            <div class="card-label">최종 자산</div>
            <div class="card-value">{result_back_test["have_money"]:,.0f}원</div>
        </div>
        <div class="card">
            <div class="card-label">총 수익률</div>
            <div class="card-value">{result_back_test["profit_rate"]:+.2f}%</div>
        </div>
        <div class="card">
            <div class="card-label">MDD</div>
            <div class="card-value">{backtest_mdd:+.2f}%</div>
        </div>
        <div class="card">
            <div class="card-label">거래 회수</div>
            <div class="card-value">(매수 {result_back_test['num_buy']} / 매도 {result_back_test['num_sell']})</div>
        </div>
        <div class="card">
            <div class="card-label">승률</div>
            <div class="card-value">{result_back_test["win_rate"]:.2f}%</div>
        </div>
        <div class="card">
            <div class="card-label">평균 수익 거래</div>
            <div class="card-value">{result_back_test['avg_win_profit']:+.2f}%</div>
        </div>
        <div class="card">
            <div class="card-label">평균 손실 거래</div>
            <div class="card-value">{result_back_test['avg_loss_profit']:+.2f}%</div>
        </div>
        <div class="card">
            <div class="card-label">Buy & Hold</div>
            <div class="card-value">{result_back_test["buy_hold_rate"]:+.2f}%</div>
        </div>    
        <div class="card">
            <div class="card-label">전략 초과 수익</div>
            <div class="card-value">{result_back_test["over_rate"]:+.2f}%p</div>
        </div>    
    </div>
    """
    return backtest_cards
def get_charts_html(pipeline_cards, pipeline_html, portfolio_cards,portfolio_html, backtest_cards, backtesting_html, trade_table, heatmap_html):
    charts_html = [
        f"""
        <div class="section">
            <h2>[섹션 1] 시세 현황</h2>
            <div class="cards">
                {pipeline_cards}
            </div>
            {pipeline_html}
        </div>
        """,
        f"""
        <div class="section">
            <h2>[섹션 2] 포트폴리오</h2> 
            <div class="cards">
                {portfolio_cards}
            </div>       
            {portfolio_html}
            {heatmap_html}    
        </div>
        """,
        f"""
        <div class="section">
            <h2>[섹션 3] 백테스팅</h2>
            {backtest_cards}
            {backtesting_html}
            <h3>거래 내역</h3>
            {trade_table}
        </div>
        """
    ]
    return charts_html
def get_html(charts_html):
    today = datetime.date.today().strftime("%Y-%m-%d")
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
                table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 16px;
                background: white;
            }}

            th, td {{
                padding: 12px 18px;
                text-align: center;
                border-bottom: 1px solid #e5e7eb;
                white-space: nowrap;
            }}

            th {{
                background-color: #f8f9fa;
                font-weight: 700;
            }}

            tr:hover {{
                background-color: #f9fafb;
            }}
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