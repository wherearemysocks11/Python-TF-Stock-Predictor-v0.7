from build_db import build_db
from fetch_data import fetch_data
from NN import NeuralNetwork
from process_data import process_data
import numpy as np
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'  # Disable GPU

def main():
    tickers = ['^FTLC']
    countries = ['USA', 'GBR', 'EUU', 'JPN', 'CHN', 'IND']
    build_db(tickers, countries)
    df = fetch_data()
    x_train, y_train, x_val, y_val, x_test, y_test = process_data(df)
    model = NeuralNetwork(x_train[0].shape, x_train, y_train)
    model.train(x_val, y_val, epochs=100)
    
main()