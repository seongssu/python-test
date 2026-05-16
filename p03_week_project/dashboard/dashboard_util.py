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