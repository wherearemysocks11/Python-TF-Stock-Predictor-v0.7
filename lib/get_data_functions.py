import pandas as pd
import requests
from datetime import datetime

def get_url(country_code, dataset):
    base_url = "https://api.worldbank.org/v2/country"
    indicator = dataset  # Consumer Price Index indicator
    return f"{base_url}/{country_code}/indicator/{indicator}?format=json&date=1950:{datetime.now().year}"

def get_cpi(country_code):
    cpi_dataset_code = "FP.CPI.TOTL"
    try:
        response = requests.get(get_url(country_code, cpi_dataset_code))
        response.raise_for_status()

        data = response.json()
        # World Bank API returns data in [metadata, actual_data] format
        df = pd.DataFrame(data[1])
        return df
    
    except Exception as e:
        print(f"Error downloading CPI data: {e}")
        return None
    
def get_gdp(url):
    try:
        pass
    
    except Exception as e:
        print(f"Error downloading GDP data: {e}")
        return None
    
def get_interest_rate():    
    try:
        pass
        
    except Exception as e:
        print(f"Error downloading interest rate data: {e}")
        return None
    
