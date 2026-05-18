import pandas as pd
import sqlite3

class DataManager:
    def __init__(self):
        pass
    
    def create_database(self):
        
        conn = sqlite3.connect('three_weeks_crypto_data.db')
        
        return conn
    
    def save_to_database(self, db_df, table_name):
        
        conn = self.create_database()        
        
        db_df.to_sql(f"{table_name}", conn, if_exists = 'replace', index = False)
                    
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        
        conn.close()
        
        return count
    
    def load_from_database(self, table_name):
        conn = sqlite3.connect('three_weeks_crypto_data.db')

        columns_info = pd.read_sql_query(
            f"PRAGMA table_info({table_name})",
            conn
        )
        columns = columns_info["name"].tolist()

        query = f"SELECT * FROM {table_name}"

        order_columns = []
        if "date" in columns:
            order_columns.append("date")
        if "ticker" in columns:
            order_columns.append("ticker")

        if order_columns:
            query += " ORDER BY " + ", ".join(order_columns)

        df = pd.read_sql_query(query, conn)

        conn.close()
        return df
    
    def db_pipeline(self):
                
        db_data = []
        #days_candle_data는 각 티커마다 데이터프레임이 들어있지만
        #결국 dict구조입니다. 
        #그래서 꺼내서 전체를 dataframe형태로 만들어 줍니다.
        for ticker, df in self.days_candle_data.items():
            db_df_for = df.copy()
            db_df_for["ticker"] = ticker
            db_df_for["date"] = db_df_for.index
            db_df_for = db_df_for[["date", "ticker"] + list(df.columns)]
            
            db_data.append(db_df_for)
            
        db_df = pd.concat(db_data)
        
        return db_df
    def add_columns(self, days_candle_data, column_name, dataframe):
        for ticker, data in dataframe.items():
            days_candle_data[ticker][column_name] = data
        return days_candle_data  
    
    def dataframe_from_dicts(self, dict_data):
        db_from_dict = []
        for ticker, data in dict_data.items():
            df_from_dict = data.copy()
            df_from_dict["ticker"] = ticker
            df_from_dict["date"] = df_from_dict.index
            
            db_from_dict.append(df_from_dict)
        result_db = pd.concat(db_from_dict, ignore_index= False)
        return result_db
    
    def dicts_from_dataframe(self, db_days_candle_data):
        db_days_candle_data["date"] = pd.to_datetime(db_days_candle_data["date"])

        dict_from_db = {}

        for ticker, df in db_days_candle_data.groupby("ticker"):
            ticker_df = df.copy()
            ticker_df = ticker_df.drop(columns=["ticker"])
            ticker_df = ticker_df.set_index("date")

            dict_from_db[ticker] = ticker_df

        return dict_from_db
    
    def dataframe_from_dict(self, current_prices):        

        db_from_dict = []

        for ticker, data in current_prices.items():
            row = data.copy()

            row["ticker"] = ticker

            db_from_dict.append(row)

        result_db = pd.DataFrame(db_from_dict)

        return result_db
    def dict_from_dataframe(self, df):
        result_dict = {}

        for _, row in df.iterrows():
            row_dict = row.to_dict()

            ticker = row_dict.pop("ticker")

            result_dict[ticker] = row_dict

        return result_dict
    
    def conversion_from_current_prices(self, data_dict, column_name):
        return {
        ticker: {column_name: value}
        for ticker, value in data_dict.items()
        }
    def filter_days(self, df, days):
        return (
            df
            .groupby("ticker", group_keys=False)
            .tail(days + 1)
        )