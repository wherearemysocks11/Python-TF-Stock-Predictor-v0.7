import schedule
import time
from config import AUTO_START
import main 

def run_main():
    main.main() 

schedule.every().day.at(AUTO_START).do(run_main)

while True:
    schedule.run_pending()
    time.sleep(1)