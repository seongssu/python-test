import sqlite3
import pandas as pd

def create_database():
    
    conn = sqlite3('crypto_data.db')
    
    return conn