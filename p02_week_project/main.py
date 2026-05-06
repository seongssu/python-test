from UpbitAPI import Upbit_API
from IPython.display import display
from basic_func import conversion_df
from Analyzer_Upbit import Analyzer_Upbit
from basic_func import error_handling
import pandas as pd

tickers = ["KRW-BTC","KRW-ETC","KRW-XRP"]
count = 30
upbit_api = Upbit_API(tickers)

#30일간 tickers의 캔들 데이터 수집
multi_candle_prices = upbit_api.get_multi_candle_data(count)
df_multi_candle_prices = pd.DataFrame(multi_candle_prices)
#(price-change) 컬럼 생성
analyzer_upbit = Analyzer_Upbit(df_multi_candle_prices)
price_minus_change = analyzer_upbit.get_price_change()



