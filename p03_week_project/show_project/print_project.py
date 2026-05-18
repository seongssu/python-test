import datetime

def print_data_pipeline(result_current_prices):
    
    first_ticker = list(result_current_prices.keys())[0]
    base_date = datetime.date.today()
    
    print(f"=== 암호화폐 현황 요약 (기준일 : {base_date}) ===\n")
    print(f"종목{"현재가":>17}{"7일 수익률":>10}{"30일 수익률":>10}{"연환산 변동성":>10}")
    print("-"*80)
    
    for ticker, data in result_current_prices.items():
        str_current_prices = data["current_prices"]
        str_return_rate_seven = data["return_rate_seven"]
        str_return_rate_thirty = data["return_rate_thirty"]  
        str_volatility_n_percent = data["volatility_n"] * 100
        
        print(f"{ticker}{str_current_prices:>15,.0f}원{str_return_rate_seven:>+12}%{str_return_rate_thirty:>+13}%{str_volatility_n_percent:>15.2f}%")
        
def print_portfolio( result_portfolio, result_single):
    days = 90
    date_today = datetime.date.today()
    date_start = date_today - datetime.timedelta(days= days)
    print("=== 포트폴리오 성과 요약 ===")
    print(f"투자 기간 {":":>5} {date_start} ~ {date_today} ({days}일)" )
    print(f"초기 자산 {":":>5} {result_single['result_single_portfolio']['invest_total_money']:,.0f} 원")
    print(f"현재 자산 {":":>5} {result_single['result_single_portfolio']['current_total_money']:,.0f} 원")
    print(f"총 수익률 {":":>5} {result_single['result_single_portfolio']['total_profit']:+.2f}%")
    print(f"MDD {":":>11} {result_single['result_single_portfolio']['mdd']:+.2f}%\n")
    print(f"종목별 기여도:")
    for ticker, data in result_portfolio.items():
        print(f"{ticker:>10} {"수익률":>5} {data["return_rate"]:>+7.2f}% {"기여":>5} {data["current_profit_weight"]:+7.2f}%p")
        
def print_back_test(trade_history):
    print("=== 거래 내역 ===")
    print(f"{"#":>3} {"유형":>3}{"날짜":>10}{"단가":>16}{"수량":>8}{"금액":>15}")  
    print(f"-"*65)        
    for index, data in trade_history.items():  
        if data["profit_have_buy"] == "":
            profit_have_buy = ""
        else:
            profit_have_buy = f"({data["profit_have_buy"]:+.2f})%"      
        print(f"{index:>3} {data['state']:>3}{data['date'].strftime('%Y-%m-%d'):>12}{data['close']:>15,.0f} 원{data['coin_count']:>10.5f}{data['trade_money']:>15,.0f} 원 {profit_have_buy:>5}")
    print(f"총 {len(trade_history)}번 거래")

def print_result_back_test(portfolio, result_back_test, mdd):
    print("=== 백테스팅 결과 ===")
    print(f"기간{':':>15} {portfolio['period']}일")
    print(f"초기 자본{':':>10} {portfolio['have_money']:,.0f}원")
    print(f"최종 자산{':':>10} {result_back_test['have_money']:,.0f}원")
    print(f"총 수익률{':':>10} {result_back_test['profit_rate']:+.2f}% ")
    print(f"MDD{':':>16} {mdd:>+.2f}%")
    print(f"총 거래{':':>12} {result_back_test['total_trade']}회 (매수 {result_back_test['num_buy']} / 매도 {result_back_test['num_sell']})")
    print(f"승률{':':>15} {result_back_test['win_rate']:.2f}%")
    print(f"평균 수익 거래{':':>5} {result_back_test['avg_win_profit']:+.2f}%")
    print(f"평균 손실 거래{':':>5} {result_back_test['avg_loss_profit']:+.2f}%")
    print(f"-" * 60 )
    print(f"Buy & Hold{':':>9} {result_back_test['buy_hold_rate']:+.2f}%")
    print(f"전략 초과 수익{':':>5} {result_back_test['over_rate']:+.2f}%p")