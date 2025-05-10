from build_db import build_db
import sqlite3 as sql
from fetch_data import fetch_data, build_query

def main():
    con = sql.connect("data.db")
    build_db(con)
    con.commit()
    print(fetch_data(con, build_query(con)))    
    con.close()

main()