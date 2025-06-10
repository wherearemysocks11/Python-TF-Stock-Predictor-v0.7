from build_db import build_db
from fetch_data import fetch_data
from NN import NeuralNetwork
from process_data import *
from sklearn.preprocessing import StandardScaler
import numpy as np
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'  # Disable GPU



def main():
    tickers = ['^FTLC']
    countries = ['USA', 'GBR', 'EUU', 'JPN', 'CHN', 'IND']
    windowSize = 5

    build_db(tickers, countries)
    df = fetch_data()

    x_train, y_train, x_val, y_val = process_data(df, windowSize)

    model = NeuralNetwork(input_shape=x_train[0].shape)
    model.train(x_train, y_train, x_val, y_val, epochs=5)

    prediction_data, scaler = get_prediction_data(df, windowSize)
    prediction = model.predict(prediction_data)
    
    prediction_reshaped = np.zeros((1, df.shape[1]))
    prediction_reshaped[0, 0] = prediction[0][0]
    
    unscaled_prediction = scaler.inverse_transform(prediction_reshaped)[0, 0]
    print(f"\nPredicted tomorrow's close price: £{unscaled_prediction:.2f}")

main()