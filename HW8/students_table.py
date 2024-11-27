from connection import create_connection
import sqlite3

def insert_students(db_name, first_name, last_name,city_id):
    sql = ''' INSERT INTO students 
    (first_name,last_name,city_id) VALUES (?,?,?)'''
    try:
        with create_connection(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql,(first_name, last_name,city_id))
            connection.commit()
    except sqlite3.Error as e:
        print(e)

