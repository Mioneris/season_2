from connection import create_connection
import sqlite3
from insert_tables import insert_categories,insert_stores,insert_products
from creating_tables import sql_to_create_products_table,sql_to_create_stores_table,sql_to_create_categories_table

def create_table(db_name, create_table_sql):
    try:
        with create_connection(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

database_name = 'categ_prod_stores.db'

# create_connection(database_name)

# create_table(database_name,sql_to_create_categories_table
# create_table(database_name,sql_to_create_products_table)
# create_table(database_name,sql_to_create_stores_table)

# insert_categories(database_name,('FD'),'FOOD PRODUCTS')
# insert_categories(database_name,('CL'),'CLOTHES')
# insert_categories(database_name,('EL'),'ELECTRONICS')

# insert_stores(database_name,(1),('ASIA'))
# insert_stores(database_name,(2),('GLOBUS'))
# insert_stores(database_name,(3),('SPAR'))

insert_products(database_name,('Fries Chiken'),'FD',210,2,1)
insert_products(database_name,('Bread'),'FD',12,2,1)
insert_products(database_name,('Sauce'),'FD',15,2,1)
insert_products(database_name,('JEANS'),'CL',11,2,2)
insert_products(database_name,('Jeans Jacket'),'CL',100,2,2)
insert_products(database_name,('Nike Air Yeezy'),'CL',110,2,2)
insert_products(database_name,('Video Card GeForce 999'),'EL',14,2,3)
insert_products(database_name,('IPhone 22 ULTRA PRO MAX'),'EL',150,2,3)
insert_products(database_name,('Xiaomi TOP'),'EL',140,2,3)






