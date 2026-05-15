import numpy as np
import pandas as pd

class AnalyzerUpbit:
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
    
    def get_ma(self, day):
        ma_data = {}
    
        for ticker, data in self.days_candle_data.items():
            ma_data[ticker] = data["close"].rolling(day).mean()
        return ma_data
    
    def get_volatility(self, day):
        
        volatility_d = {}
        std = {}
        for ticker, data in self.days_candle_data.items():
            
            change_price = data["close"].pct_change()
            #std_data :일별 수익률의 변동성
            std_data = change_price.rolling(day).std()
            std[ticker] = data["close"].tail(day).std()
            profit_day = std_data.iloc[-1] * np.sqrt(252)           
            
            volatility_d [ticker] = round(float(profit_day), 2)
        
        return volatility_d, std 
    
    def get_upper_band(self, ma_data, std):
        upper_band = {}
        for ticker in ma_data:
            upper_band[ticker] = ma_data[ticker] + (std[ticker] * 2)
        return upper_band
    
    def get_lower_band(self, ma_data, std):
        lower_band = {}
        for ticker in ma_data:
            lower_band[ticker] = ma_data[ticker] - (std[ticker] * 2) 
        return lower_band
    
    # 90일 전에 구매한 코인 종목들의 최대낙폭(mdd) 계산
    def get_mdd(self, portfolio):
        days_portfolio_prices = None
        
        for ticker, data in portfolio.items():
            amount = data["amount"]
            df = self.days_candle_data[ticker]
            
            close_price = df["close"].iloc[0]
            buy_coin_count = amount / close_price
            
            days_my_coin_prices = df["close"] * buy_coin_count
            
            if days_portfolio_prices is None:
                days_portfolio_prices = days_my_coin_prices
            else:
                days_portfolio_prices += days_my_coin_prices
                
            self.days_candle_data[ticker]["portfolio_value"] = days_my_coin_prices
        days_max_coin_prices = days_portfolio_prices.cummax()
        drop_from_max = ((days_portfolio_prices - days_max_coin_prices)) / days_max_coin_prices
        mdd = drop_from_max.min() * 100
        
        return mdd, days_portfolio_prices
    
    def get_portfolio_values(self,portfolio, return_rate_ninety):
        current_total_money = 0
        invest_total_money = 0
        result_portfolio = {}
        for ticker, data in portfolio.items():
            amount = data["amount"]
            weight = data["weight"]
            return_rate = return_rate_ninety[ticker]
            
            profit_money = (amount * return_rate) /100
            profit_total_money = amount + profit_money
            
            invest_total_money += amount
            current_total_money += profit_total_money
            
            result_portfolio[ticker] = {
                "portfolio_weight" : weight * 100,
                "invest_money" : amount,
                "return_rate" : return_rate,
                "profit_money" : profit_money,
                "profit_total_money" : profit_total_money
            }
        for ticker, data in result_portfolio.items():
            data["current_weight"] = (data["profit_total_money"] / current_total_money) * 100  
            data["current_profit_weight"] = (data["profit_money"] / invest_total_money) * 100
        total_profit = ((current_total_money/invest_total_money) - 1) * 100
        return result_portfolio, invest_total_money, current_total_money, total_profit
    
    def get_profit_days(self):
        profit_days_by_ticker = {}
        for ticker, data in self.days_candle_data.items():
            profit_days_by_ticker[ticker] = data["close"].pct_change()
        return profit_days_by_ticker
    
    def get_trade_history(self, portfolio, coin_count = 0, have_coin = False):
        condition_buy_sell = self.get_back_test()
        fee_rate = portfolio["fee"] / 100
        have_money = portfolio["have_money"]
        
        trade_history = {}
        num = 0
        for index, data in condition_buy_sell.iterrows():
            
            if data["buy_condition"] and not have_coin:
                buy_money = have_money * (1 - fee_rate)
                coin_count = buy_money / data["close"]
                have_money = 0
                have_coin = True
                num += 1
                trade_history[num] = {
                    "state": "매수",
                    "date": index,
                    "close": data["close"],
                    "coin_count": coin_count,
                    "trade_money": buy_money
                }              
                
            elif data["sell_condition"] and have_coin:
                have_money = coin_count * data["close"] * (1 - fee_rate )            
                have_coin = False
                num +=1
                trade_history[num] = {
                    "state": "매도",
                    "date": index,
                    "close": data["close"],
                    "coin_count": coin_count,
                    "trade_money": have_money
                }    
                coin_count = 0
                
        if have_coin:
            last_price = condition_buy_sell.iloc[-1]["close"]
            have_money = coin_count * last_price * (1 - fee_rate)
            coin_count = 0
            have_coin = False
            
        profit_rate = ((have_money / portfolio["have_money"]) - 1) * 100

        return trade_history, have_money, profit_rate

    def get_back_test(self):
        days_candle_data = self.days_candle_data["KRW-BTC"]
        days_candle_data["buy_condition"] = (
            (days_candle_data["ma5"].shift(1) <= days_candle_data["ma20"].shift(1)) &
            (days_candle_data["ma5"] > days_candle_data["ma20"])
        )
        
        days_candle_data["sell_condition"] = (
            (days_candle_data["ma5"].shift(1) >= days_candle_data["ma20"].shift(1)) &
            (days_candle_data["ma5"] < days_candle_data["ma20"])
        )
        return days_candle_data