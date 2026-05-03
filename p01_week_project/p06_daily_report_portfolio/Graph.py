import matplotlib.pyplot as plt

class Graph:
    def __init__(self, candle_data):
        self.candle_data = candle_data
        
    def get_graph_coin_profit(self):

        coin_price_change = self.candle_data[::-1]
        coin_price = []
        coin_date = []

        for item in coin_price_change:
            date = item["candle_date_time_kst"]
            price = item["trade_price"]
            split_date = date.split("T")[0]
            slice_date = split_date[2:]
            
            coin_price.append(price)
            coin_date.append(slice_date)

        #print(f"날짜가격 : {coin_date}")
        plt.plot(coin_date,coin_price, label="MA7")
        plt.show()