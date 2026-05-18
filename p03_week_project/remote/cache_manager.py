import sqlite3
import pandas as pd
import datetime
class CacheManager:
    def __init__(self):
        self.today = datetime.date.today()
    
    def get_cache(self, ticker, table_name):
        conn = sqlite3.connect("three_weeks_crypto_data.db")
        
        query = f"""
        SELECT COUNT(*)
        FROM {table_name}
        WHERE ticker =?
        AND substr(date, 1, 10) = ?
        """
        
        try:
            cursor = conn.cursor()
            cursor.execute(query, (ticker, str(self.today)))
            count = cursor.fetchone()[0]
            
        except sqlite3.OperationalError:
            count = 0
            
        conn.close()
        
        return count > 0
    
    def load_cache(self, ticker, table_name):
        conn = sqlite3.connect("three_weeks_crypto_data.db")
        
        query = f"""
        SELECT *
        FROM {table_name}
        WHERE ticker = ?
        ORDER BY date
        """
        
        df = pd.read_sql_query(query, conn, params=(ticker,))
        conn.close()
        
        df["date"] = pd.to_datetime(df["date"])
        df = df.set_index("date")
        
        if "ticker" in df.columns:
            df = df.drop(columns=["ticker"])
            
        return df