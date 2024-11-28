sql_to_create_categories_table = '''
CREATE TABLE categories (
    code VARCHAR(2) PRIMARY KEY, --FD
    title VARCHAR(150) NOT NULL);'''


sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(250) NOT NULL,
    category_code VARCHAR(2) NOT NULL,
    unit_price REAL NOT NULL,
    stock_quantity INTEGER NOT NULL,
    store_id INTEGER NOT NULL,
    FOREIGN KEY (category_code) REFERENCES categories (code),
    FOREIGN KEY (store_id) REFERENCES stores (store_id));'''


sql_to_create_stores_table = '''
CREATE TABLE stores(
    store_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL)'''

