from graph import graph
from basic_func import conversion_datetime

def p_three(result_all_data):
    
    result_all_data["candle_date_time_kst"] = conversion_datetime(result_all_data["candle_date_time_kst"])
    
    result_data = result_all_data.sort_values(
        ["ticker", "candle_date_time_kst"]
    )
    
    result_grouby_ticker = result_data.groupby("ticker")
    
    graph(result_grouby_ticker)