from lib.get_ticker_data import getTickerData
from lib.get_data_functions import getData
from config import DMA_PERIODS
from concurrent.futures import ThreadPoolExecutor, as_completed
import sqlite3
import os

def process_country(country):
    """Process data for a single country."""
    try:
        data = getData(country)
        data.cpi()
        data.gdp()
        data.ir()
        return f"Successfully collected data for {country}"
    except Exception as e:
        return f"Error collecting data for {country}: {e}"

def process_ticker(ticker):
    """Process data for a single ticker."""
    try:
        ticker_data = getTickerData(ticker, DMA_PERIODS)
        ticker_data.ticker_to_db()
        return f"Successfully collected data for {ticker}"
    except Exception as e:
        return f"Error collecting data for {ticker}: {e}"

def build_db(tickers, countries):
    """Build the database with parallel processing for faster data collection."""
    try:
        with ThreadPoolExecutor() as executor:
            # Process countries in parallel
            print("Collecting country data...")
            country_futures = [executor.submit(process_country, country) 
                             for country in countries]
            
            for future in as_completed(country_futures):
                print(future.result())

            # Process tickers in parallel
            print("\nCollecting ticker data...")
            ticker_futures = [executor.submit(process_ticker, ticker) 
                            for ticker in tickers]
            
            for future in as_completed(ticker_futures):
                print(future.result())

        print("\nDatabase build process completed.")
    
    except Exception as e:
        print(f"Error in building the database: {e}")
        raise

def build_prediction_db(db_path='prediction_results.db'):
    """Create a new database for storing daily predictions and actual close prices with clear column names."""
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS daily_predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                ticker TEXT NOT NULL,
                tomorrows_predicted_close REAL NOT NULL,
                todays_close REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
        print(f"Prediction results database created at {db_path}")
    else:
        print(f"Prediction results database already exists at {db_path}.")