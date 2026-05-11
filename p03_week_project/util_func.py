import time

def retry_call_api(py_data, retry = 3, delay = 1, *tickers, **days):
    for index in range(1, retry + 1):
        try:
            
            if py_data is None:
                raise ValueError("데이터가 없습니다.")
            
            return py_data
        
        except Exception as e:
            print(f"{index}번째 호출 실패 : {e}")
            
            if index == retry:
                print("3회 호출에 실패했습니다.")
                return None
            time.sleep(delay)


def convert_str_to_list(str_data):
    convert_data = []
    for data in str_data:
        convert_data.append(data)
    return convert_data