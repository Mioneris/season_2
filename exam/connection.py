import sqlite3

def create_connection(db_name):
    try:
        connection = sqlite3.connect(db_name)
        return connection
    except sqlite3.Error as e:
        print(e)
        return None