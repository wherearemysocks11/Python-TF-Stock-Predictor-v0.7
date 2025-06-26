import schedule
import time
from config import AUTO_START
import main  # Import the main module

def run_main():
    main.main()  # Assuming there's a main() function in main.py

schedule.every().day.at(AUTO_START).do(run_main)

while True:
    schedule.run_pending()
    time.sleep(1)