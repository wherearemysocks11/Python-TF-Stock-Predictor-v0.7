import sqlite3
from datetime import datetime

def log_prediction(date, ticker, predicted_close, actual_close=None, db_path='prediction_results.db'):
    """
    Log the prediction and actual close price to the prediction_results.db database.
    If actual_close is not available, it can be set to None and updated later.
    """
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        INSERT INTO daily_predictions (date, ticker, predicted_close, actual_close, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (date, ticker, predicted_close, actual_close, datetime.now()))
    conn.commit()
    conn.close()
    print(f"Logged prediction for {ticker} on {date}: predicted_close=£{predicted_close:.2f}, actual_close={actual_close}")
