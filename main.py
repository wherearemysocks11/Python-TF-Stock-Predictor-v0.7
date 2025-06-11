from lib.build_db import build_db
from lib.fetch_data import fetch_data
from lib.NN import NeuralNetwork
from lib.process_data import process_data, get_prediction_data
from config import *
import os

os.environ['CUDA_VISIBLE_DEVICES'] = CUDA_VISIBLE_DEVICES

def main():
    try:
        # Build database
        print("Building database...")
        build_db(TICKERS, COUNTRIES)

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
        
        # Train model
        print("Training model...")
        model = NeuralNetwork(input_shape=x_train[0].shape)
        history = model.train(x_train, y_train, x_val, y_val, epochs=EPOCHS)
        
        # Print training results
        final_loss = history.history['loss'][-1]
        final_val_loss = history.history['val_loss'][-1]
        print(f"\nTraining Results:")
        print(f"Final Loss: {final_loss:.4f}")
        print(f"Final Validation Loss: {final_val_loss:.4f}")

        # Make prediction
        print("\nMaking prediction...")
        prediction_data = get_prediction_data(df, scaler, WINDOW_SIZE)
        prediction = model.predict(prediction_data, scaler, df.shape[1])
        print(f"Predicted tomorrow's close price: £{prediction:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
