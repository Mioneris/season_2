import sqlite3

# def create_connection(db_name):
#     connection = None
#     try:
#         connection = sqlite3.connect(db_name)
#     except sqlite3.Error as e:
#         print(e)
#     return connection

def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_products(db_name, products):
    sql = ''' INSERT INTO products
    (product_title,price,quantity)
    VALUES (?,?,?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, products)
    except sqlite3.Error as e:
        print(e)
def update_products(db_name, products):
    sql = '''UPDATE products SET quantity = ? where id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, products)
    except sqlite3.Error as e:
        print(e)

def update_price_products(db_name, products):
    sql = '''UPDATE products SET price = ? where id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, products)
    except sqlite3.Error as e:
        print(e)
def delete_products(db_name, id):
    sql = ''' 
    DELETE FROM products WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
    except sqlite3.Error as e:
        print(e)

def select_all_products(db_name):
    sql = '''SELECT * FROM products'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def price_filter(db_name, price_limit, quantity_limit):
    sql = '''SELECT * FROM products WHERE price < ? AND quantity > ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql,( price_limit, quantity_limit))
            rows = cursor.fetchall()
            if rows:
                print("Найденные товары:")
                for row in rows:
                    print(row)
            else:
                print('Товарны не найдены.')
    except sqlite3.Error as e:
        print(e)

def key_word_filter(db_name, key_word):
    sql = '''SELECT * FROM products WHERE product_title LIKE ? '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, ('%' + key_word + '%',))
            rows = cursor.fetchall()
            if rows:
                print('Найденные товары:')
                for row in rows:
                    print(row)
            else:
                print('Товары не найдены.')
    except sqlite3.Error as e:
        print(e)



sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price  FLOAT(10,2) NOT NULL DEFAULT 0.0,
    quantity INT NOT NULL DEFAULT 0
    )
'''

data_base_name = 'products.db'
# connection = create_connection(data_base_name)
# create_table(data_base_name, sql_to_create_products_table)
# if connection is not None:
#     print('Connection successful')
#     connection.close()
# insert_products(data_base_name,('Процессор AMD Ryzen 5 5500', 8224, 19))
# insert_products(data_base_name,('Процессор AMD Ryzen 5 7600X ', 19159, 36))
# insert_products(data_base_name,('Процессор AMD Ryzen 7 9700X ', 34285, 52))
# insert_products(data_base_name,('Процессор Intel Core i7-14700K', 39326, 68))
# insert_products(data_base_name,('Видеокарта GeForce GTX1650', 15630, 25))
# insert_products(data_base_name,('Видеокарта GEFORCE RTX3050', 18554, 38))
# insert_products(data_base_name,('Видеокарта GEFORCE RTX4060', 33982, 63))
# insert_products(data_base_name,('Видеокарта GEFORCE RTX4080 SUPER 16GB', 99617, 34))
# insert_products(data_base_name,('Материнская плата MB AM5 GIGABYTE B650M', 12504, 40))
# insert_products(data_base_name,('Материнская плата MB AM5 ASUS TUF GAMING B650M-PLUS', 18957, 55))
# insert_products(data_base_name,('Материнская плата MB LGA1151 Asus H110M-K', 5382, 20))
# insert_products(data_base_name,('Материнская плата MB LGA1151v2 BIOSTAR B365MHC Intel B8365', 7124, 26))
# insert_products(data_base_name,('Монитор LCD 23.8" Hikvision 1080P', 7254, 15))
# insert_products(data_base_name,('Монитор LCD 27" Elista ELS-I27VFH', 11259, 20))
# insert_products(data_base_name,('Монитор LG 27MP400-B/27"', 16927, 33))
# select_all_products(data_base_name)
# update_products(data_base_name,(20, 1))
# update_price_products(data_base_name, (9000, 1))
# delete_products(data_base_name, 1)
# price_filter(data_base_name, 10000,20)
# key_word_filter(data_base_name, 'Видеокарта')











