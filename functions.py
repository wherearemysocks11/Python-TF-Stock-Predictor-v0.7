import yfinance as yf

def get_ticker_data(ticker):
    try:
        ticker_data = yf.download(ticker)

        return ticker_data
    
    except Exception as e:
        print(f"Error downloading ticker data: {e}")
        return None

def get_uk_cpi_data():
    try:
        url = "https://www.ons.gov.uk/generator?format=csv&uri=/economy/inflationandpriceindices/timeseries/d7g7/mm23"

    except Exception as e:
        print(f"Error downloading CPI data: {e}")
        return None
        

def get_uk_interest_rate_data():    
    try:
        url = "https://www.bankofengland.co.uk/boeapps/database/Bank-Rate.asp"
        
    except Exception as e:
        print(f"Error downloading interest rate data: {e}")
        return None
    
def calc_ticker_DMA(ticker_close, period):
    try:
        dma = ticker_close.rolling(window=period).mean()

        return dma
    
    except Exception as e:
        print(f"Error calculating DMA: {e}")
        return None

def get_gdp_data():
    try:
        url = "https://www.ons.gov.uk/generator?format=csv&uri=/economy/grossdomesticproductgdp/timeseries/ybha/pn2"
    
    except Exception as e:
        print(f"Error downloading GDP data: {e}")
        return None

