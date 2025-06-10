from build_db import build_db
from fetch_data import fetch_data
from NN import NeuralNetwork
from process_data import *
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'  # Disable GPU



def main():
    tickers = ['^FTLC']
    countries = ['USA', 'GBR', 'EUU', 'JPN', 'CHN', 'IND']
    windowSize = 5

    # Create plots directory if it doesn't exist
    if not os.path.exists('plots'):
        os.makedirs('plots')

    build_db(tickers, countries)
    df = fetch_data()

    x_train, y_train, x_val, y_val, scaler = process_data(df, windowSize)

    model = NeuralNetwork(input_shape=x_train[0].shape)
    model.train(x_train, y_train, x_val, y_val, epochs=500)

    prediction_data = get_prediction_data(df, scaler, windowSize)
    prediction = model.predict(prediction_data, scaler, df.shape[1])
    print(f"\nPredicted tomorrow's close price: £{prediction:.2f}")

main()