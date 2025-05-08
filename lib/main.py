from get_data_functions import getData
from get_ticker_data import getTickerData

def main():
    countries = ['GBR', 'EUU', 'USA']
    for country in countries:
        print(f"Collecting data for {country}...")
        data = getData(country)
        data.cpi()
        data.gdp()
        data.ir()
        print(f"Finished collecting data for {country}.\n")
    
    print("Collecting data for ticker ^FTLC...")
    ticker_data = getTickerData('^FTLC')
    ticker_data.ticker_to_db(5)
    print("Finished collecting data for ticker ^FTLC.")

    

main()