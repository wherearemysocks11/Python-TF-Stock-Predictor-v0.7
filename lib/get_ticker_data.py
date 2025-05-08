import yfinance as yf
import sqlite3 as sql

def get_ticker_data(ticker):
    try:
        ticker_data = yf.download(ticker)
        return ticker_data
    
    except Exception as e:
        print(f"Error downloading ticker data: {e}")
        return None
    
def get_ticker_DMA(ticker_close, period):
    try:
        dma = ticker_close.rolling(window=period).mean()
        return dma
    
    except Exception as e:
        print(f"Error calculating DMA: {e}")
        return None

def tickerDMA_to_db(ticker, DMAperiod):
    try:
        con = sql.connect("data.db")

        ticker_data = get_ticker_data(f'{ticker}')
        ticker_data[('DMA', f'{ticker}')] = get_ticker_DMA(ticker_data.Close, DMAperiod)

        ticker_data.to_sql('ticker', con, if_exists='replace')
        
    except Exception as e:
        print(f"Error passing ticker and DMA to database: e")