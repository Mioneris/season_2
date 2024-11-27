from connection import create_connection
from creating_tables import (
    sql_to_create_countries_table,
    sql_to_create_cities_table,
    sql_to_create_students_table)
from cities_table import insert_cities
from countries_table import insert_countries
from students_table import insert_students
import sqlite3

def create_table(db_name, create_table_sql):
    try:
        with create_connection(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

database_name = 'countries_cities_students.db'

# create_connection(database_name)


# create_table(database_name, sql_to_create_countries_table)
# create_table(database_name,sql_to_create_cities_table)
# create_table(database_name,sql_to_create_students_table)



# insert_countries(database_name,'France')
# insert_countries(database_name,'Germany')
# insert_countries(database_name,'Canada')

# insert_cities(database_name,'Paris', 105.4, 1 )
# insert_cities(database_name,'Bastia', 19.38, 1 )
# insert_cities(database_name,'Berlin', 891.8, 2 )
# insert_cities(database_name,'Hamburg', 755, 2 )
# insert_cities(database_name,'Munchen', 310.4, 2 )
# insert_cities(database_name,'Toronto', 630.2, 3 )
# insert_cities(database_name,'Ottawa', 2.778, 3 )

# insert_students(database_name,'Peter', 'Parker', 1)
# insert_students(database_name,'Barry', 'Allen', 2)
# insert_students(database_name,'Morty', 'Smith', 3)
# insert_students(database_name,'Ronald','McDonald', 4)
# insert_students(database_name,'Noah','Cyrus', 5)
# insert_students(database_name,'James Jonah','Jameson', 6)
# insert_students(database_name,'Jack','Jackson', 7)
# insert_students(database_name,'Otto','Octavius', 1)
# insert_students(database_name,'Bruce','Wayne', 2)
# insert_students(database_name,'Norman','Osborn', 3)
# insert_students(database_name,'Stephen ','Strange', 4)
# insert_students(database_name,'Tony ','Stark', 5)
# insert_students(database_name,'Steve ','Rogers', 6)
# insert_students(database_name,'Robert Bruce ','Banner', 7)
# insert_students(database_name,'Wade ','Wilson', 1)












