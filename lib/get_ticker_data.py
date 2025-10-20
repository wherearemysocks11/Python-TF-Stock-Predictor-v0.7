import yfinance as yf
import sqlite3 as sql
import pandas as pd
from datetime import datetime, timedelta


class getTickerData:
    def __init__(self, ticker, dma_periods):
        self.ticker = ticker
        self.dma_periods = dma_periods

    def get_data(self):
        try:
            # Get end date (today)
            end_date = pd.Timestamp.now()
            # Set start date to maximum possible historical date (1970-01-01)
            start_date = pd.Timestamp('1970-01-01')
            
            print(f"Downloading {self.ticker} data from {start_date.date()} to {end_date.date()}")
            print("(Note: Will get all available data regardless of start date)")
            
            # Download maximum available historical data
            # yfinance's download() sometimes changes signatures; keep args conservative
            attempts = 3
            ticker_data = None
            for attempt in range(1, attempts + 1):
                try:
                    ticker_data = yf.download(
                        self.ticker,
                        start=start_date,
                        end=end_date,
                        progress=False,
                        actions=True,  # Include dividends and stock splits
                        auto_adjust=True  # Automatically adjust prices for splits
                    )
                    break
                except TypeError as te:
                    # Older/newer yfinance may not accept certain kwargs; retry without them
                    if attempt == 1:
                        print(f"yfinance TypeError on attempt {attempt}: {te} - retrying without 'actions'/'auto_adjust' args")
                        try:
                            ticker_data = yf.download(self.ticker, start=start_date, end=end_date, progress=False)
                            break
                        except Exception:
                            ticker_data = None
                    else:
                        ticker_data = None
                except Exception as e:
                    print(f"yfinance error on attempt {attempt}: {e}")
                    ticker_data = None

            if ticker_data is None:
                raise Exception("Failed to download ticker data after multiple attempts")
            
            if ticker_data.empty:
                print(f"Warning: No data downloaded for {self.ticker}")
                return None
            
            # Log the actual date range we got
            date_range = ticker_data.index
            print(f"Successfully downloaded {len(ticker_data)} rows of data for {self.ticker}")
            print(f"Data spans from {date_range[0].date()} to {date_range[-1].date()}")
            print(f"Total trading days: {len(ticker_data)}")
            print(f"Years of data: {(date_range[-1] - date_range[0]).days / 365.25:.1f}")
            
            # Verify we have enough data for DMAs
            max_dma = max(self.dma_periods) if self.dma_periods else 0
            if len(ticker_data) < max_dma:
                print(f"Warning: Downloaded data ({len(ticker_data)} days) is less than longest DMA period ({max_dma} days)")
            
            return ticker_data
        except Exception as e:
            print(f"Error downloading ticker data for {self.ticker}: {e}")
            print("Please check if the ticker symbol is correct and if you have internet connectivity")
            return None

    def calculate_dma(self, close_prices, period):
        try:
            dma = close_prices.rolling(window=period).mean()
            return dma
        except Exception as e:
            print(f"Error calculating DMA for {self.ticker}: {e}")
            return None

    def ticker_to_db(self):
        try:
            data = self.get_data()
            if data is None:
                print(f"No data to save for {self.ticker}; skipping database write.")
                return
            data.columns = [col[0].lower() if isinstance(col, tuple) else col.lower() for col in data.columns]
            for period in self.dma_periods:
                data[f'dma_{period}'] = self.calculate_dma(data.close, period)
            
            data.index = data.index.date
            data.index.name = 'date'
            
            table_name = f"ticker_{self.ticker.replace('^', '').replace('-', '_')}"
            with sql.connect("data.db") as con:
                data.to_sql(table_name, con, if_exists='replace', index=True)
            print(f"Successfully saved {self.ticker} data with DMAs {self.dma_periods} to table {table_name}")
        except Exception as e:
            print(f"Error saving {self.ticker} data to database: {e}")