import sqlite3

from main_creating_tables import database_name

def select_city(db_name):
    sql = "SELECT id, title FROM cities"
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            cities = cursor.fetchall()
            for city in cities:
                print(f'Город - {city[1]} , ID - {city[0]}')
    except sqlite3.Error as e:
        print(e)

def select_student(db_name,city_id):
    sql = """SELECT s.first_name,
    s.last_name,
    c.title AS country,
    ci.title AS city,
    ci.area 
    FROM students s
    JOIN cities ci ON s.city_id = ci.id
    JOIN countries c ON ci.country_id = c.id
    WHERE city_id = ?
    """

    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql,(city_id,))
            students = cursor.fetchall()

            if students:
                for student in students:
                    print(f'Имя: {student[0]} , Фамилия: {student[1]},'
                          f'страна: {student[2]}, город проживания: {student[3]},'
                          f'площадь города: {student[4]} ')
            else:
                print('Студенты отсутствуют в данном городе')
    except sqlite3.Error as e:
        print(e)

def search_student():
    while True:
        try:
            print("Вы можете отобразить список учеников\n"
                  "по выбранному id города из перечня\n"
                  "городов ниже\n(для выхода "
                  "из программы введите 0)")
            select_city(database_name)

            search = input("Введите ID города:").strip()
            search = int(search)

            if search == 0:
                print('Программа завершена')
                break
            if 1 <= search <= 7:
                select_student(database_name,search)
            else:
                print("Ошибка: введите ID города в диапозоне от 1 до 7")

        except ValueError as e:
            print(f'Ошибка: {e}')

search_student()