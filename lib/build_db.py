from get_ticker_data import getTickerData
from get_data_functions import getData

def build_db(tickers, countries):
    try:
        for country in countries:
            try:
                print(f"Collecting data for {country}...")
                data = getData(country)
                data.cpi()
                data.gdp()
                data.ir()
                print(f"Finished collecting data for {country}.\n")
            except Exception as e:
                print(f"Error building {country} database: {e}")
                continue

        dma_periods = [5, 10, 50, 200, 365]
        
        for ticker in tickers:
            try:
                print(f"Collecting data for {ticker}...")
                ticker_data = getTickerData(ticker, dma_periods)
                ticker_data.ticker_to_db()
                print(f"Finished collecting data for {ticker}.\n")
            except Exception as e:
                print(f"Error building {ticker} database: {e}")
                continue

        print("Database build process completed.")
    
    except Exception as e:
        print(f"Error in building the database: {e}")