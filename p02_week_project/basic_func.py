import pandas as pd
import requests
import matplotlib.dates as mdates
from Sqlite_Upbit import Sqlite_Upbit

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

def formatting_time(chart_result):
    chart_result.xaxis.set_major_formatter(
            mdates.DateFormatter("%m-%d")
        )
    
    
def save_sqlite_db(result_p_one, result_p_two):
    ### DataFrame 데이터 합치기 ###
    result_all_data = pd.merge(result_p_one, result_p_two, on= ["ticker", "candle_date_time_kst"])
    #print(result_all_data)

    # ### SQLite DB ###

    # dataframe 모두 db에 저장하기
    sqlite_upbit = Sqlite_Upbit(result_all_data)
    sqlite_upbit.save_to_database()