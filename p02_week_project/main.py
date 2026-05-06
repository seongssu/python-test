from UpbitAPI import Upbit_API
from IPython.display import display
from basic_func import conversion_df
from Analyzer_Upbit import Analyzer_Upbit
from basic_func import error_handling
import pandas as pd

tickers = ["KRW-BTC","KRW-ETC","KRW-XRP"]
count = 30
upbit_api = Upbit_API(tickers)

###문제 1번###

#30일간 tickers의 캔들 데이터 수집
multi_candle_prices = upbit_api.get_multi_candle_data(count)
df_multi_candle_prices = pd.DataFrame(multi_candle_prices)


analyzer_upbit = Analyzer_Upbit(df_multi_candle_prices)

#(price-change) 컬럼 생성
price_minus_change = analyzer_upbit.get_price_change()

#변동률 계산
pct_price_minus_change = analyzer_upbit.get_price_change_pct()

#print(f"컬럼확인 : {df_multi_candle_prices.columns}")

#일 중 변동폭 계산
high_low_diff = analyzer_upbit.get_high_low_diff()

print(
    analyzer_upbit.df_multi_candle_prices[
        [
            "market",
            "price_change",
            "price_change_pct",
            "high_low_diff"
        ]
    ]
)

###문제 2번###