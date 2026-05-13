import pandas as pd
import sqlite3

class DataManager:
    def __init__(self, days_candle_data):
        self.days_candle_data = days_candle_data
    
    def add_columns(self, column_name, dataframe):
        for ticker, data in dataframe.items():
            self.days_candle_data[ticker][column_name] = data
        return self.days_candle_data
    
    def to_dataframe(self, dict_data):
        db_from_dict = []
        for ticker, data in dict_data.items():
            df_from_dict = data.copy()
            df_from_dict["ticker"] = ticker
            df_from_dict["date"] = df_from_dict.index
            
            db_from_dict.append(df_from_dict)
            result_db = pd.concat(db_from_dict, ignore_index= False)
        return result_db
    
    def create_database(self):
        
        conn = sqlite3.connect('three_weeks_crypto_data.db')
        
        return conn
    
    def save_to_database(self, db_df):
        
        conn = self.create_database()        
        
        db_df.to_sql("three_weeks_crypto_data", conn, if_exists = 'replace', index = False)
                    
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM three_weeks_crypto_data")
        count = cursor.fetchone()[0]
        
        conn.close()
        
        return count
    
    def load_from_database(self):
        
        conn = sqlite3.connect('three_weeks_crypto_data.db')
        
        query = "SELECT * FROM three_weeks_crypto_data ORDER BY date, ticker"
        df = pd.read_sql_query(query, conn)
        
        conn.close()
        
        return df
    
    def db_pipeline(self):
        columns = [
            'open', 'close', 'current_prices',
            'return_rate_one', 'return_rate_seven', 'return_rate_thirty',
            'ma5', 'ma20', 'ma60', 'volatility_n',
            'upper_band', 'lower_band', 'category'
        ]
        
        db_data = []
        #days_candle_data는 각 티커마다 데이터프레임이 들어있지만
        #결국 dict구조입니다. 
        #그래서 꺼내서 전체를 dataframe형태로 만들어 줍니다.
        for ticker, df in self.days_candle_data.items():
            db_df_for = df[columns].copy()
            db_df_for["ticker"] = ticker
            db_df_for["date"] = db_df_for.index
            db_df_for = db_df_for[["date", "ticker"] + columns]
            
            db_data.append(db_df_for)
            
        db_df = pd.concat(db_data)
        self.save_to_database(db_df)