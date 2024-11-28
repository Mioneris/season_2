import sqlite3

from main_creating_tables import database_name

def select_store(db_name):
    sql = "SELECT store_id, title FROM stores"
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            stores = cursor.fetchall()
            for store in stores:
                print(f'Store - {store[1]},', 'ID - ', store[0])
    except sqlite3.Error as e:
        print(e)

def select_stores(db_name,store_id):
    sql = """SELECT p.title AS product_name,
    c.title AS category_name,
    p.unit_price AS price,
    p.stock_quantity AS quantity
    FROM products p
    JOIN categories c ON p.category_code = c.code
    JOIN stores s ON p.store_id = s.store_id
    WHERE p.store_id = ?
    """

    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql,(store_id,))
            products = cursor.fetchall()

            if products:
                print(f"продукты в магазине ID {store_id} - {products[0][1]}")
                for products in products:
                    print(f'Названия: {products[0]}')
                    print(f"Категория: {products[1]}")
                    print(f"Цена: {products[2]}")
                    print(f"Количество на складе: {products[3]}")
                    print("-" * 40)
            else:
                print(f"Продукты в магазине ID {store_id} не найдены.")
    except sqlite3.Error as e:
        print(e)

def search_product():
    while True:
        try:
            print("Вы можете отобразить список продуктов\n"
                  "по выбранному ID магазина из перечня\n"
                  "магазинов ниже\n(для выхода из программы введите 0):")\

            select_store(database_name)

            search = input("Введите ID магазина: ").strip()
            search = int(search)

            if search == 0:
                print('Программа завершена')
                break
            if 1 <= search <= 3:
                select_stores(database_name,search)
            else:
                print("Ошибка: введите ID города в диапозоне от 1 до 7")

        except ValueError as e:
            print(f'Ошибка: {e}')

search_product()