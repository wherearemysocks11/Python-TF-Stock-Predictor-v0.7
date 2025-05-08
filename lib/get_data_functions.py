import pandas as pd
import requests
from datetime import datetime

def get_url(country_code, dataset):
    try:
        base_url = "https://api.worldbank.org/v2/country"
        indicator = dataset  # Consumer Price Index indicator
        return f"{base_url}/{country_code}/indicator/{indicator}?format=json&date=1950:{datetime.now().year}"
    except Exception as e:
        print(f"Error constructing URL for {country_code} {dataset}: {e}")
        return None

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
        print(f"Error downloading CPI data for {country_code}: {e}")
        return None
    
def get_gdp(country_code):
    try:
        gdp_dataset_code = "NY.GDP.MKTP.CD"
        response = requests.get(get_url(country_code, gdp_dataset_code))
        response.raise_for_status()

        data = response.json()
        # World Bank API returns data in [metadata, actual_data] format
        df = pd.DataFrame(data[1])
        return df
    
    except Exception as e:
        print(f"Error downloading GDP data for {country_code}: {e}")
        return None
    
def get_ir(country_code):    
    try:
        ir_dataset_code = "FR.INR.RINR"
        response = requests.get(get_url(country_code, ir_dataset_code))
        response.raise_for_status()

        data = response.json()
        # World Bank API returns data in [metadata, actual_data] format
        df = pd.DataFrame(data[1])
        return df
        
    except Exception as e:
        print(f"Error downloading interest rate data for {country_code}: {e}")
        return None
    

    
