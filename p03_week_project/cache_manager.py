import sqlite3

class CacheManager:
    def __init__(self, ticker):
        self.ticker = ticker
    
    def get_cache(self):
        conn = sqlite3.connect("three_weeks_crypto_data.db")
        
        query = """
        SELECT COUNT(*)
        FROM three_weeks_crypto_data
        WHERE ticker =?
        AND substr(date, 1, 10)
        """
        
        try:
            cursor = conn.cursor()
            cursor.execute(query, (self.ticker, str(self.today)))
            count = cursor.fetchone()[0]
            
        except sqlite3.OperationalError:
            count = 0
            
        conn.close()
        
        return count > 0