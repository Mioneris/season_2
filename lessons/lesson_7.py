import sqlite3

# def create_connection(db_name):
#     connection = None
#     try:
#         connection = sqlite3.connect(db_name)
#     except sqlite3.Error as e:
#         print(e)
#     return connection
#
# def create_table(connection, create_table_sql):
#     try:
#         cursor = connection.cursor()
#         cursor.execute(create_table_sql)
#     except sqlite3.Error as e:
#         print(e)

# def insert_employee(connection, employee):
#     sql = ''' INSERT INTO employees
#     (full_name,salary,hobby,birth_date,is_married)
#     VALUES (?,?,?,?,?)'''
#     try:
#         cursor = connection.cursor()
#         cursor.execute(sql, employee)
#         connection.commit()
#     except sqlite3.Error as e:
#         print(e)

def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_employees(db_name, employee):
    sql = ''' INSERT INTO employees
    (full_name,salary,hobby,birth_date,is_married)
    VALUES (?,?,?,?,?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, employee)
    except sqlite3.Error as e:
        print(e)

def update_employee(db_name, employee):
    sql = ''' 
    UPDATE employees SET salary = ?, is_married = ? 
    WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, employee)
    except sqlite3.Error as e:
        print(e)

def delete_employee(db_name, id):
    sql = ''' 
    DELETE FROM employees WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
    except sqlite3.Error as e:
        print(e)

def select_all_employees(db_name):
    sql = '''SELECT * FROM employees'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def select_employees_by_salary(db_name,salary_limit):
    sql = '''SELECT * FROM employees WHERE salary >= ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql,(salary_limit,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


sql_to_create_employees_table = '''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(200) NOT NULL,
    salary FLOAT(10,2) NOT NULL DEFAULT 0.0,
    hobby TEXT DEFAULT NULL,
    birth_date DATE NOT NULL,
    is_married BOOLEAN DEFAULT FALSE
    )
'''

database_name = 'season_2.db'
# my_connection = create_connection(database_name)
# if my_connection is not None:
#     print('Connection successful to database!')
#     # create_table(my_connection, sql_to_create_employees_table)
#     insert_employee(my_connection,
#                     ('Jibek Manasova', 2400.5,'programming', '2000-01-25', False ))
#     my_connection.close()

# create_table(database_name,sql_to_create_employees_table)4
# insert_employees(database_name,
#                  ('Jibek Manasova', 2400.5,'programming', '2000-01-25', False ))
# insert_employees(database_name,
#                  ('Peter parker', 2000.0, 'science', '2000-05-24', True ))

# update_employee(database_name,(2500, True,  2))

# delete_employee(database_name, 1)
# select_all_employees(database_name)
# select_employees_by_salary(database_name,2000)