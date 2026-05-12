import plotly.graph_objects as go
from plotly.subplots import make_subplots

def graph (days_candle_data):
    
    subplot_titles = [
        f"{ticker}   "
        f"{df['current_prices'].iloc[-1]:,.0f}원   "
        f"{df['return_rate_seven'].iloc[-1]:+.2f}%"
        for ticker, df in days_candle_data.items()
    ]
    
    fig = make_subplots(rows = 2, cols = 2, subplot_titles= subplot_titles)
    
    colors = {
        "close": "rgba(139, 69, 19, 0.3)",     
        "ma5": "rgba(255, 165, 0, 0.5)",       
        "ma20": "rgba(139, 69, 19, 0.3)",      
        "ma60": "rgba(255, 105, 180, 0.3)"
    }
    
    for i, (ticker, columns) in enumerate(days_candle_data.items()):
        columns = columns.reset_index()

        row = i // 2 + 1
        col = i % 2 + 1

        show_legend = i == 0

        fig.add_trace(
            go.Scatter(
                x=columns["date"],
                y=columns["lower_band"],
                mode="lines",
                line=dict(width=0),
                showlegend=False
            ),
            row=row,
            col=col
        )

        fig.add_trace(
            go.Scatter(
                x=columns["date"],
                y=columns["upper_band"],
                mode="lines",
                fill="tonexty",
                fillcolor="rgba(100, 100, 255, 0.3)",
                line=dict(width=0),
                showlegend=False
            ),
            row=row,
            col=col
        )

        for column in ["close", "ma5", "ma20", "ma60"]:
            fig.add_trace(
                go.Scatter(
                    x=columns["date"],
                    y=columns[column],
                    mode="lines",
                    name=column,
                    line=dict(color=colors[column]),
                    showlegend=show_legend
                ),
                row=row,
                col=col
            )

    fig.show()
    