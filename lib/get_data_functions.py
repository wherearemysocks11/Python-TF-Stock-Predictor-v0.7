import pandas as pd
import requests
from datetime import datetime
import sqlite3 as sql

class getData:
    def __init__(self, country_code):
        self.country_code = country_code
        self.con = sql.connect("data.db")

    def get_url(self, dataset):
        try:
            base_url = "https://api.worldbank.org/v2/country"
            return f"{base_url}/{self.country_code}/indicator/{dataset}?format=json&frequency=D&date=1950:{datetime.now().year}"
        except Exception as e:
            print(f"Error constructing URL for {self.country_code} {dataset}: {e}")
            return None
   
    def pop_data(self, data):
        try:
            df = pd.DataFrame(data[1])
            processed_df = df[['date', 'value']]
            return processed_df
            
        except Exception as e:
            print(f"Error processing data: {e}")
            return None

    def cpi(self):
        cpi_dataset_code = "FP.CPI.TOTL.ZG"
        try:
            response = requests.get(self.get_url(cpi_dataset_code))
            response.raise_for_status()
            data = response.json()
            df = self.pop_data(data)
            self.save_to_db(df, 'cpi')
            return df
        except Exception as e:
            print(f"Error downloading CPI data for {self.country_code}: {e}")
            return None

    def gdp(self):
        gdp_dataset_code = "NY.GDP.MKTP.CD"
        try:
            response = requests.get(self.get_url(gdp_dataset_code))
            response.raise_for_status()
            data = response.json()
            df = self.pop_data(data)
            self.save_to_db(df, 'gdp')
            return df
        except Exception as e:
            print(f"Error downloading GDP data for {self.country_code}: {e}")
            return None

    def ir(self):
        ir_dataset_code = "FR.INR.RINR"
        try:
            response = requests.get(self.get_url(ir_dataset_code))
            response.raise_for_status()
            data = response.json()
            df = self.pop_data(data)
            self.save_to_db(df, 'ir')
            return df
        except Exception as e:
            print(f"Error downloading interest rate data for {self.country_code}: {e}")
            return None

    def save_to_db(self, data, indicator):
        try:
            if data is not None and not data.empty:
                table_name = f'{indicator}_{self.country_code.lower()}'
                data.to_sql(table_name, self.con, if_exists='replace', index=False)
        except Exception as e:
            print(f"Error saving {indicator} data to database: {e}")

    def __del__(self):
        self.con.close()
