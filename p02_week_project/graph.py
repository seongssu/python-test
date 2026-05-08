import matplotlib.pyplot as plt

def graph(result_grouby_ticker):
    
    for ticker, column in result_grouby_ticker:
        
        column.plot(
            x = "candle_date_time_kst",
            y = ["trade_price", "ma5"],
            kind = "line",
            title = ticker
        )
        
        plt.show()