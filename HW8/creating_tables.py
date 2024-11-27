sql_to_create_cities_table = '''
CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    area FLOAT DEFAULT 0,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries (id)
    );
'''

sql_to_create_countries_table = '''
CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
    );
'''
#При попытке создать таблицу студентов выходила ошибка.
# Для себя на этом этапе открыл,
                                 #что в правом верхнем углу необходимо переключаться
                                    #между БД для при использовании функции

sql_to_create_students_table = '''
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES cities (id)
    );
'''
