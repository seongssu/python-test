import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def p_three(result_all_data):
    
    result_all_data = result_all_data.sort_values(
        ["ticker", "candle_date_time_kst"]
    )
    
    result_grouby_ticker = result_all_data.groupby("ticker")
    
    for ticker, column in result_grouby_ticker:
        
        column.plot(
            x = "candle_date_time_kst",
            y = ["trade_price", "ma5"],
            kind = "line",
            title = ticker
        )
        
        plt.show()
        
        
        
     