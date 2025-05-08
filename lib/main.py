from get_data_functions import getData
from get_ticker_data import getTickerData
import sqlite3 as sql

def main():
    con = sql.connect("data.db")
    countries = ['GBR', 'EUU', 'USA']
    for country in countries:
        print(f"Collecting data for {country}...")
        data = getData(country)
        data.cpi()
        data.gdp()
        data.ir()
        print(f"Finished collecting data for {country}.\n")
        
        query = """
        SELECT 
            cpi_gbr.date AS date,
            cpi_gbr.value AS cpi_gbr,
            gdp_gbr.value AS gdp_gbr,
            ir_gbr.value AS ir_gbr,
            cpi_euu.value AS cpi_euu,
            gdp_euu.value AS gdp_euu,
            ir_euu.value AS ir_euu,
            cpi_usa.value AS cpi_usa,
            gdp_usa.value AS gdp_usa,
            ir_usa.value AS ir_usa,
            ticker.Open AS ticker_open,
            ticker.High AS ticker_high,
            ticker.Low AS ticker_low,
            ticker.Close AS ticker_close,
            ticker.Volume AS ticker_volume,
            ticker."dma_5" AS ticker_dma5
        FROM cpi_gbr
        LEFT JOIN gdp_gbr ON cpi_gbr.date = gdp_gbr.date
        LEFT JOIN ir_gbr ON cpi_gbr.date = ir_gbr.date
        LEFT JOIN cpi_euu ON cpi_gbr.date = cpi_euu.date
        LEFT JOIN gdp_euu ON cpi_gbr.date = gdp_euu.date
        LEFT JOIN ir_euu ON cpi_gbr.date = ir_euu.date
        LEFT JOIN cpi_usa ON cpi_gbr.date = cpi_usa.date
        LEFT JOIN gdp_usa ON cpi_gbr.date = gdp_usa.date
        LEFT JOIN ir_usa ON cpi_gbr.date = ir_usa.date
        LEFT JOIN ticker ON cpi_gbr.date = ticker.date
        ORDER BY cpi_gbr.date;
        """

main()