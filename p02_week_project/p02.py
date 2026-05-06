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
close_for_ticker = db_close_five_days.groupby("market")["trade_price"].rolling(5).mean()
#결측치 확인
check_close_for_ticker = close_for_ticker.isnull()

print(f"5일간 이동평균선\n{close_for_ticker}")
print(f"결측치 수 : {check_close_for_ticker}")
