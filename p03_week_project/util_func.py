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

    
    