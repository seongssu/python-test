import time

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

def print_basic_statistics(day_candle_data):
    
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