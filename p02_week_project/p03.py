import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from graph import graph

def p_three(result_all_data):
    
    result_all_data = result_all_data.sort_values(
        ["ticker", "candle_date_time_kst"]
    )
    
    result_grouby_ticker = result_all_data.groupby("ticker")
    
    graph(result_grouby_ticker)