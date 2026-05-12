import pandas as pd

class DataManager:
    def __init__(self, days_candle_data):
        self.days_candle_data = days_candle_data
    
    def add_columns(self, column_name, dataframe):
        for ticker, data in dataframe.items():
            self.days_candle_data[ticker][column_name] = data
        return self.days_candle_data