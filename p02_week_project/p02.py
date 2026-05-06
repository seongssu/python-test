from UpbitAPI import Upbit_API
from IPython.display import display
from basic_func import conversion_df
from Analyzer_Upbit import Analyzer_Upbit
from basic_func import error_handling
import pandas as pd

tickers = ["KRW-BTC","KRW-ETC","KRW-XRP"]
count = 30

upbit_api = Upbit_API(tickers)

close_five_days = upbit_api.get_multi_candle_data(count)
db_close_five_days = pd.DataFrame(close_five_days)
#ticker별 close기준 데이터를 구해야하므로 그룹화 합니다.
#5일씩 이동 평균을 계산합니다.
close_for_ticker = db_close_five_days.groupby("market")

#결측치 처리(fillna) : 결측치 -> 해당날짜의 close값으로 대체하기
db_close_five_days["ma5"] = None
for market, group in db_close_five_days.groupby("market"):
    ma5 = group["trade_price"].rolling(5).mean()
    
    ma5 = ma5.fillna(group["trade_price"])
## ▶ 주의 : 아래처럼 하면 market이 다른걸로 넘어가면 처음부터 다시 덮어쓴다. 
##    db_close_five_days["ma5"] = ma5
    db_close_five_days.loc[group.index, "ma5"] = ma5
    
print(db_close_five_days["ma5"])