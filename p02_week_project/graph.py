import matplotlib.pyplot as plt
from basic_func import formatting_time
def graph(result_grouby_ticker):
    
    fig, axes = plt.subplots(3, 1, figsize = (10, 20))

    for ax, (ticker, column) in zip(axes, result_grouby_ticker):
        
        chart_result = column.plot(
            x = "candle_date_time_kst",
            y = ["trade_price", "ma5"],
            kind = "line",
            title = ticker,
            style = ["-", "--"],
            alpha = 0.5,
            ax = ax
        )        
        
        formatting_time(chart_result)
    plt.subplots_adjust(hspace= 0.8)    
    plt.show()