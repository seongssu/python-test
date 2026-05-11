
class Analyzer_Upbit:
    def __init__(self, current_price, days_candle_data):
        self.current_price = current_price
        self.days_candle_data = days_candle_data

    def get_return_rate_d(self, days_ago):
        
        return_rate_d = {}
        for ticker, current_price in self.current_price.items():
            
            df = self.days_candle_data[ticker]
            days_ago_price = df.iloc[-(days_ago + 1)]["close"]
            
            days_age_profit_rate = ((current_price - days_ago_price) / days_ago_price) * 100
            
            
            return_rate_d[ticker] = round(float(days_age_profit_rate), 2)
        return return_rate_d
            