import matplotlib.pyplot as plt

def graph (days_candle_data):
    
    fig, axes = plt.subplots(2,2, figsize = (10, 20))
    
    for ax, (ticker, columns) in zip(axes.flatten(), days_candle_data.items()):
        columns = columns.reset_index()
        
        ax.fill_between(
            columns["index"],
            columns["lower_band"],
            columns["upper_band"],
            alpha = 0.2
        )
        
        columns.plot(
            x = "index",
            y = ["close", "ma5", "ma20", "ma60"],
            kind = "line",
            title = "종목명 + 현재가 + 7일 수익률",
            alpha = 0.4,
            ax = ax
        )
        
    plt.subplots_adjust(hspace= 0.8)
    plt.show()