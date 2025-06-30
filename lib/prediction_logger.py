import sqlite3
from datetime import datetime

def log_prediction(date, ticker, tomorrows_predicted_close, todays_close=None, db_path='prediction_results.db'):
    """
    Log tomorrow's predicted close and today's close price to the prediction_results.db database.
    If todays_close is not available, it can be set to None and updated later.
    """
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        INSERT INTO daily_predictions (date, ticker, tomorrows_predicted_close, todays_close, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (date, ticker, tomorrows_predicted_close, todays_close, datetime.now()))
    conn.commit()
    conn.close()
    print(f"Logged prediction for {ticker} on {date}: tomorrows_predicted_close=£{tomorrows_predicted_close:.2f}, todays_close={todays_close}")
