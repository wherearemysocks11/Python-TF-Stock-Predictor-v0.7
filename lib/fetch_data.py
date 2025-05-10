import sqlite3 as sql
import pandas as pd

con = sql.connect("data.db")
cursor = con.cursor()

def get_all_tables(cursor):
    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        return [table[0] for table in cursor.fetchall()]
    except Exception as e:
        print(f"Error fetching tables: {e}")
        return []

def get_table_columns(cursor, table_name):
    try:
        cursor.execute(f"PRAGMA table_info({table_name})")
        return [column[1] for column in cursor.fetchall()]
    except Exception as e:
        print(f"Error fetching columns for table {table_name}: {e}")
        return []
    
def build_query():
    try:
        print("Building query...")
        tables = get_all_tables(cursor)

        select_parts = []
        for table in tables:
            columns = get_table_columns(cursor, table)
            for column in columns:
                # Skip date columns but keep them for JOIN conditions
                if column.lower() != 'date':
                    select_parts.append(f'{table}."{column}"')
            
        query = f"SELECT {', '.join(select_parts)}"
        query += f" FROM ticker"
        
        for table in tables[1:]:
            query += f" LEFT JOIN {table} ON ticker.date = {table}.date"
        
        query += " ORDER BY ticker.date DESC"
        
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
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
