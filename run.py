import schedule
import time
from config import AUTO_START
import main  # Import the main module
import datetime

def run_main():
    # Only run on weekdays (Monday=0, Sunday=6)
    today = datetime.datetime.now()
    if today.weekday() >= 5:  # 5=Saturday, 6=Sunday
        print("Market closed: skipping run (weekend)")
        return
    from lib.build_db import build_prediction_db
    build_prediction_db()  # Ensure the prediction results DB exists before running main
    main.main()  # Assuming there's a main() function in main.py

schedule.every().day.at(AUTO_START).do(run_main)

while True:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] Waiting for {AUTO_START}... Press Ctrl+C to exit.")
    schedule.run_pending()
    time.sleep(60)