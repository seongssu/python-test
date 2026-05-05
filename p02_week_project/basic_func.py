import pandas as pd
import requests

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
        
        