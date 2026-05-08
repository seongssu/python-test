import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from basic_func import fomatting_time
def graph(result_grouby_ticker):
    
    for ticker, column in result_grouby_ticker:
        
        chart_result = column.plot(
            x = "candle_date_time_kst",
            y = ["trade_price", "ma5"],
            kind = "line",
            title = ticker
        )        
        
        fomatting_time(chart_result)
        
        plt.show()