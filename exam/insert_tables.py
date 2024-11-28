from connection import create_connection
import sqlite3
def insert_categories(db_name,code, title):
    sql = ''' INSERT INTO categories 
    (code, title) VALUES (?,?)'''
    try:
        with create_connection(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (code, title))
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def insert_products(db_name, title, category_code,unit_price,stock_quantity,store_id):
    sql = ''' INSERT INTO products 
    (title, category_code,unit_price,stock_quantity,store_id) 
    VALUES (?,?,?,?,?)'''
    try:
        with create_connection(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (title, category_code,unit_price,stock_quantity,store_id))
            connection.commit()
    except sqlite3.Error as e:
        print(e)


def insert_stores(db_name,store_id, title):
    sql = ''' INSERT INTO stores 
    (store_id, title) VALUES (?,?)'''
    try:
        with create_connection(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (store_id, title))
            connection.commit()
    except sqlite3.Error as e:
        print(e)
