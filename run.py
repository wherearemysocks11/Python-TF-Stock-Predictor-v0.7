import schedule
import time
from config import AUTO_START
import main  # Import the main module
import datetime

def run_main():
    # Only run on days except Friday (4) and Saturday (5)
    today = datetime.datetime.now()
    if today.weekday() in [4, 5]:  # 4=Friday, 5=Saturday
        print("Market closed: skipping run (Will next run on Sunday)")
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