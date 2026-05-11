import requests
import pyupbit

def error_handling(response_data):
    try:        
        if not response_data:
            raise ValueError("데이터가 존재하지 않습니다.")
        
        return response_data
    
    except Exception as e:
        print(f"ERROR : {e}")
        
    return None

def convert_str_to_list(str_data):
    convert_data = []
    for data in str_data:
        convert_data.append(data)
    return convert_data