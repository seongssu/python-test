import pandas as pd
import requests
import pandas as pd
import matplotlib.dates as mdates

def conversion_df (dict_data):
    df = pd.DataFrame(dict_data)
    
    return df

def error_handling(url, params, headers):
    try:
        response = requests.get(url, params= params, headers= headers)
        response.raise_for_status()
        
        data = response.json()    
    
        if not data:
                raise ValueError("데이터가 존재하지 않습니다.")
        
        return data
    
    except Exception as e:
        print(f"ERROR : {e}")
        
    return None            

def conversion_datetime(time_data):
    time_data = pd.to_datetime(time_data)
    return time_data           

def fomatting_time(chart_result):
    chart_result.xaxis.set_major_formatter(
            mdates.DateFormatter("%m-%d")
        )