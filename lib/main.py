from build_db import build_db
from fetch_data import fetch_data

def main():
    build_db()
    print(fetch_data())

main()