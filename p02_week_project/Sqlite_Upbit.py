import sqlite3
from pandas import pd

def create_database():
    
    conn = sqlite3('crypto_data.db')
    
    return conn