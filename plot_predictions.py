import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def plot_predictions(db_path='prediction_results.db'):
    """
    Query the daily_predictions table and plot predicted vs actual close prices.
    """
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query('SELECT date, predicted_close, actual_close FROM daily_predictions ORDER BY date ASC', conn)
    conn.close()

    if df.empty:
        print("No data found in the database.")
        return

    df['date'] = pd.to_datetime(df['date'])
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['predicted_close'], label='Predicted Close', marker='o')
    plt.plot(df['date'], df['actual_close'], label='Actual Close', marker='x')
    plt.xlabel('Date')
    plt.ylabel('Close Price (£)')
    plt.title('Predicted vs Actual Close Prices')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_predictions()
