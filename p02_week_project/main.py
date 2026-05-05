from UpbitAPI import Upbit_API
from IPython.display import display

def collect_market_data():
    #시장 데이터 수집 함수
    
    #주요 암호화폐 선택
    
    major_tickers = ["KRW-BTC", "KRW-ETC", "KRW-XRP"]
    print(f"분석 대상 티커 : {major_tickers} \n")
    
    upbit_api = Upbit_API(major_tickers)
    #현재가 조회
    current_prices = upbit_api.get_current_prices()
    print(f"현재가 정보 \n")
    for ticker, price in current_prices.items():
        print(f"{ticker} : {price:.0f}원")
        
    #캔들데이터 수집(최근 30일)
    count = 30
    candle_data = upbit_api.get_multi_candle_data(count)
    
    print(f"수집된 데이터 행 수 : {len(candle_data)}")
    print(f"데이터 컬럼 : {list(candle_data.columns)}")
    return candle_data, current_prices

raw_data, prices = collect_market_data()
#print(raw_data.head(10))

key = raw_data.groupby('ticker')
print(key.groups.keys())
print(key.groups.values())

for key, each_df in raw_data.groupby('ticker'):
    print(key)
    display(each_df.head(2))
