import yfinance as yf
import sqlite3 as sql


class getTickerData:
    def __init__(self, ticker, dma_periods):
        self.ticker = ticker
        self.dma_periods = dma_periods

    def get_data(self):
        try:
            ticker_data = yf.download(self.ticker)
            return ticker_data
        except Exception as e:
            print(f"Error downloading ticker data for {self.ticker}: {e}")
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