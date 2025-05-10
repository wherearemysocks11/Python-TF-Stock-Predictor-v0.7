from build_db import build_db
from fetch_data import fetch_data

def main():
    tickers = ['^FTLC']
    countries = ['USA', 'GBR', 'EUU', 'CAN', 'AUS', 'JPN', 'CHN', 'IND']
    build_db(tickers, countries)
    print(fetch_data())

main()