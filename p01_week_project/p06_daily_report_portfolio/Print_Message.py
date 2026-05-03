

class Print_Message:
    def __init__(self, portfolio_analysis, max_coin_name, profit_rate):
        self.portfolio_analysis = portfolio_analysis
        self.max_coin_name = max_coin_name
        self.profit_rate = profit_rate
        
    def print_message(self):
        
        print(f"\n\n {"코인":<10} {"수량":>5} {"현재가":>21} {"가치":>20} {"비중":>14}")
        print("-" * 100)
        
        for x in self.portfolio_analysis:
            stocks = x["코인"]
            volumes = x["수량"]
            current_price = x["현재가격"]
            value = x["가치"]
            ratio = x["비중"]
            stocks_name = stocks.split("-")[1]
            print(f"{stocks_name:<10} {volumes:>10}{stocks_name} {current_price:>20,.0f}원 {value:>20,.0f}원 {ratio:>15.1f}%")
        
        coin_profit = max(self.profit_rate, key=lambda x: x["profit"])
        print(f"\n최고수익코인 : {coin_profit["ticker"]}")        
        print(f"보유 비중 상위 1개 코인 : {self.max_coin_name}")