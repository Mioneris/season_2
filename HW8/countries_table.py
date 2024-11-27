from connection import create_connection
import sqlite3

def insert_countries(db_name, country_title):
    sql = ''' INSERT INTO countries (title) VALUES (?)'''
    try:
        with create_connection(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql,(country_title,))
            connection.commit()
    except sqlite3.Error as e:
        print(e)



