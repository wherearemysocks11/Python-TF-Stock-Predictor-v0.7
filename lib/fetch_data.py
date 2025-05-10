import sqlite3 as sql
import pandas as pd

def get_all_tables(cursor):
    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        return [table[0] for table in cursor.fetchall()]
    except Exception as e:
        print(f"Error fetching tables: {e}")
        return []
    
def build_query(con):
    try:
        cursor = con.cursor()
        print("Building query...")
        tables = get_all_tables(cursor)

        select_parts = []
        for table in tables:
            cursor.execute(f"PRAGMA table_info({table})")
            columns = cursor.fetchall()
            for column in columns:
                column_name = column[1]
                if column_name.lower() != 'date':
                    select_parts.append(f'"{table}"."{column_name}" as "{table}_{column_name}"')
        
        query = f"SELECT {', '.join(select_parts)} FROM ticker"
        
        for table in tables:
            if table != 'ticker':
                query += f' LEFT JOIN "{table}" ON "ticker".date = "{table}".date'
        
        query += ' ORDER BY "ticker".date DESC'
        return query
        
    except Exception as e:
        print(f"Error building query: {e}")
        return None
    
def fetch_data(con, query):
    try:
        print("Fetching data...")
        df = pd.read_sql_query(query, con)
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
