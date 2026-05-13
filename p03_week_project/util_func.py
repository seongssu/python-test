import time
import datetime

def retry_call_api(py_func, retry, delay, *tickers, **days):
    for index in range(1, retry + 1):
        try:
            result_py_data = py_func(*tickers, **days)
            
            if result_py_data is None:
                raise ValueError("데이터가 없습니다.")
            
            return result_py_data
        
        except Exception as e:
            print(f"{index}번째 호출 실패 : {e}\n")
            
            if index == retry:
                print("3회 호출에 실패했습니다.")
                return None
            time.sleep(delay)


def convert_str_to_list(str_data):
    convert_data = []
    for data in str_data:
        convert_data.append(data)
    return convert_data

def print_data_pipeline(day_candle_data):
    
    print(f"=== 암호화폐 현황 요약 (기준일 : {list(day_candle_data.keys())[0]}) ===\n")
    print(f"종목{"현재가":>17}{"7일 수익률":>10}{"30일 수익률":>10}{"연환산 변동성":>10}")
    print("-"*80)
    
    for ticker, data in day_candle_data.items():
        item = data.iloc[-1]
        str_current_prices = item["current_prices"]
        str_return_rate_seven = item["return_rate_seven"]
        str_return_rate_thirty = item["return_rate_thirty"]  
        str_volatility_n_percent = item["volatility_n"] * 100
        
        print(f"{ticker}{str_current_prices:>15,.0f}원{str_return_rate_seven:>+12}%{str_return_rate_thirty:>+13}%{str_volatility_n_percent:>15}%")
        
def print_portfolio(result_portfolio, invest_total_money, current_total_money, total_profit, mdd):
    days = 90
    date_today = datetime.date.today()
    date_start = date_today - datetime.timedelta(days= days)
    print("=== 포트폴리오 성과 요약 ===")
    print(f"투자 기간 {":":>5} {date_start} ~ {date_today} ({days}일)" )
    print(f"초기 자산 {":":>5} {invest_total_money:,.0f} 원")
    print(f"현재 자산 {":":>5} {current_total_money:,.0f} 원")
    print(f"총 수익률 {":":>5} {total_profit:+.2f}%")
    print(f"MDD {":":>11} {mdd:+.2f}%\n")
    print(f"종목별 기여도:")
    for ticker, data in result_portfolio.items():
        print(f"{ticker:>10} {"수익률":>5} {data["return_rate"]:>+7.2f}% {"기여":>5} {data["current_profit_weight"]:+7.2f}%p")