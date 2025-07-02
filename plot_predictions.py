import sqlite3
import matplotlib.pyplot as plt
import datetime

# Path to the prediction results database
DB_PATH = 'prediction_results.db'

def fetch_predictions():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Fetch date, ticker, and tomorrows_predicted_close from daily_predictions
    cursor.execute('''SELECT date, ticker, tomorrows_predicted_close, todays_close FROM daily_predictions ORDER BY date ASC''')
    data = cursor.fetchall()
    conn.close()
    return data

def plot_predictions():
    data = fetch_predictions()
    if not data:
        print('No prediction data found.')
        return
    dates = [datetime.datetime.strptime(row[0], '%Y-%m-%d').date() for row in data]
    predictions = [row[2] for row in data]
    closes = [row[3] for row in data]
    tickers = list(set(row[1] for row in data))
    # Offset predictions by one day to represent tomorrow's close prediction
    pred_dates = [d + datetime.timedelta(days=1) for d in dates]
    plt.figure(figsize=(12, 6))
    plt.plot(pred_dates, predictions, marker='o', linestyle='--', label='Predicted Close (Tomorrow)')  # Dotted line for predictions
    if any(closes):
        plt.plot(dates, closes, marker='x', linestyle='-', label='Actual Close')  # Solid line for actuals
    plt.xlabel('Day')
    plt.ylabel('Price')
    plt.title(f'Stock Predictions Over Time{f" ({tickers[0]})" if len(tickers)==1 else ""}')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('predictions.png')
    print('Plot saved as predictions.png')
    # plt.show()  # Disabled for headless environments

if __name__ == '__main__':
    plot_predictions()
