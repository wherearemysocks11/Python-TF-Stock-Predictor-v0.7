from lib.build_db import build_db
from lib.fetch_data import fetch_data
from lib.NN import NeuralNetwork
from lib.process_data import process_data, get_prediction_data
from lib.prediction_logger import log_prediction
from datetime import datetime
from config import *
import os

os.environ['CUDA_VISIBLE_DEVICES'] = CUDA_VISIBLE_DEVICES

def main():
    try:
        # Build database
        print("Building database...")
        build_db(TICKER, COUNTRIES)

        # Fetch and validate data
        print("Fetching data...")
        df = fetch_data()
        if df is None or df.empty:
            raise Exception("Failed to fetch data or data is empty")
        if len(df) <= WINDOW_SIZE:
            raise Exception(f"Not enough data points ({len(df)}) for window size {WINDOW_SIZE}")

        # Process data
        print("Processing data...")
        x_train, y_train, x_val, y_val, scaler = process_data(df, WINDOW_SIZE)
        prediction_data = get_prediction_data(df, scaler, WINDOW_SIZE)
        
        # Run multiple iterations of training and prediction
        predictions = []
        for i in range(NUM_PREDICTIONS):
            print(f"\nTraining Model {i+1}/3...")
            model = NeuralNetwork(input_shape=x_train[0].shape)
            history = model.train(x_train, y_train, x_val, y_val, epochs=EPOCHS)
            
            # Print training results
            final_loss = history.history['loss'][-1]
            final_val_loss = history.history['val_loss'][-1]
            print(f"Training Results {i+1}:")
            print(f"Final Loss: {final_loss:.4f}")
            print(f"Final Validation Loss: {final_val_loss:.4f}")

            # Make prediction
            print(f"Making prediction {i+1}...")
            prediction = model.predict(prediction_data, scaler, df.shape[1])
            predictions.append(prediction)
            print(f"Model {i+1} prediction: £{prediction:.2f}")

        # Calculate and display average
        avg_prediction = sum(predictions) / len(predictions)
        print("\nPrediction Summary:")
        for i, pred in enumerate(predictions, 1):
            print(f"Model {i}: £{pred:.2f}")
        print(f"Average prediction: £{avg_prediction:.2f}")

        # Log prediction and today's close price
        today = datetime.now().strftime('%Y-%m-%d')
        ticker = TICKER[0] if isinstance(TICKER, list) else TICKER
        # Get today's close price from df (assume last row, first column is close)
        try:
            todays_close = float(df.iloc[-1, 0])
        except Exception:
            todays_close = None
        log_prediction(date=today, ticker=ticker, predicted_close=avg_prediction, actual_close=todays_close)

    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
