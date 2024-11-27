from connection import create_connection
import sqlite3

def insert_cities(db_name,city_title,area,country_id):
    sql = ''' INSERT INTO cities 
    (title, area, country_id) VALUES (?,?,?)'''
    try:
        with create_connection(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (city_title,area,country_id))
            connection.commit()
    except sqlite3.Error as e:
        print(e)
