from build_db import build_db
from fetch_data import fetch_data
from NN import NeuralNetwork
from process_data import process_data
import numpy as np

def main():
    tickers = ['^FTLC']
    countries = ['USA', 'GBR', 'EUU', 'JPN', 'CHN', 'IND']
    build_db(tickers, countries)
    df = fetch_data()
    x_train, y_train = process_data(df)
    print(x_train.shape)
    print(y_train.shape)
    
main()