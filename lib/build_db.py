from get_ticker_data import getTickerData
from get_data_functions import getData

def build_db(con):
    try:
        countries = ['USA', 'GBR', 'EUU', 'JPN', 'CHN', 'IND']
        for country in countries:
            print(f"Collecting data for {country}...")
            data = getData(country)
            data.cpi()
            data.gdp()
            data.ir()
            print(f"Finished collecting data for {country}.\n")

    except Exception as e:
        print(f"Error building {country} database: {e}")

    try:
        tickers = ['^FTLC']
        dma_periods = [5, 10, 50, 200, 365]  # renamed to dma_periods for clarity
        
        for ticker in tickers:
            print(f"Collecting data for {ticker}...")
            ticker_data = getTickerData(ticker, dma_periods)
            ticker_data.ticker_to_db()
            print(f"Finished collecting data for {ticker}.\n")

    except Exception as e:
        print(f"Error building {ticker} database: {e}")