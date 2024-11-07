# name = 'Rob' #Переменная с именем объекта
# age = 20 #Переменная с возрастом объекта
# height = 69.9 #Переменная с весом объекта
#
# print(name, age, height)

# access_permission = int(input('Введите свой возраст для доступа:').strip())
#
# if access_permission >= 18:
#     print('Доступ разрешен!')
#
# else:
#     print("Съебался с сайта, пездюк!")

# fruits = ['Apple', 'Banana', 'Mango', 'Orange','Strawberry']
#
# print(fruits[1::3])
#
# cities = ('Amsterdam', 'Bangkhok', 'New-York', 'Berlin', 'Paris')
#
# print(cities[0::2])
def greet():
    try:
        greet_ = str(input('Пожалуйста, введите свое имя:').strip())
        black_list = 'дурачок', 'сука', 'козел', 'урод'
        soset_bebru = 'Ильяс', 'Дарья'
        kitties = 'Беря', 'Бася'

        if greet_ in kitties:
            print(f'{greet_} хорошая пися кися')
            return

        age = int(input(f'{greet_},пожалуйста, введите свой возраст:'))

        if age >= 18:
            print(f'Пользователю {greet_} разрешен доступ!')
        else:
            print('Съебался с сайта!')
        if not greet_.isalpha():
            raise ValueError('Имя должно состоять из букв!')
        if greet_.lower()in black_list:
            print(f'Введено слово из черного списка {black_list}')
        if greet_  in soset_bebru:
            print(f'Пользователь с именем {greet_} сосет бебру')
        else:
            print(f'Привет, {greet_}!')
    except ValueError as e:
        print(e)





greet()

