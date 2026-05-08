from p01 import p_one
from p02 import p_two
from p03 import p_three
from basic_func import conversion_datetime, get_sqlite_db
###▶▶▶▶▶문제 1번◀◀◀◀◀###
# candle_date_time_kst : 거래 날짜
# ticker : 코인명 / price_change : 종가 - 시가
# price_change_pct : 변동률 / high_low_diff : 일일 변동폭
result_p_one = p_one()
result_p_one["candle_date_time_kst"] = conversion_datetime(result_p_one["candle_date_time_kst"])
print(result_p_one)

###▶▶▶▶▶문제 2번◀◀◀◀◀###
# candle_date_time_kst : 거래 날짜
# ticker : 코인명 / trade_price : 종가
# ma5 : 종가 기준 5일 이동 평균
result_p_two = p_two()
result_p_two["candle_date_time_kst"] = conversion_datetime(result_p_two["candle_date_time_kst"])
print(result_p_two)

###▶▶▶▶▶문제 3번◀◀◀◀◀###
sqlite_db = get_sqlite_db(result_p_one, result_p_two)
result_p_three = p_three(sqlite_db)
#print(f"문제3번{result_p_three}")