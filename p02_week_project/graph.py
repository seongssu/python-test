import matplotlib.pyplot as plt
from basic_func import formatting_time
def graph(result_grouby_ticker):
    
    for ticker, column in result_grouby_ticker:
        
        chart_result = column.plot(
            x = "candle_date_time_kst",
            y = ["trade_price", "ma5"],
            kind = "line",
            title = ticker,
            
            style = ["-", "--"],
            
            alpha = 0.5
        )        
        
        formatting_time(chart_result)
        
        plt.show()