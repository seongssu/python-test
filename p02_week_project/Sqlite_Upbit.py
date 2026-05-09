import sqlite3
import pandas as pd

class Sqlite_Upbit:
    def __init__(self, dataframe = None):   # dataframe 초기값을 None으로 지정해줘서 매개변수없어도 호출가능
        self.dataframe = dataframe
    def create_database(self):
        
        conn = sqlite3.connect('crypto_data.db')
        
        return conn
    
    def save_to_database(self):
        
        conn = self.create_database()
        
        db_df = self.dataframe[['candle_date_time_kst', 'ticker', 'trade_price', 'ma5','price_change', 'price_change_pct', 'high_low_diff']].copy()
        
        db_df.to_sql('crypto_ohlcv', conn, if_exists = 'replace', index = False)
        
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM crypto_ohlcv")
        count = cursor.fetchone()[0]
        
        conn.close()
        
        return count
    
    def load_from_database(self):
        
        conn = sqlite3.connect('crypto_data.db')
        
        query = "SELECT*FROM crypto_ohlcv ORDER BY candle_date_time_kst, ticker"
        df = pd.read_sql_query(query, conn)
        
        conn.close()
        return df
    
    