# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f'NAME: {self.name}, AGE: {self.age}, BIRTH YEAR: {2024 - self.age}'
#
#
# some_animal = Animal('ANIM', 3)
#
# print(some_animal.info())


class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__was_born()

    def set_age(self,age):
        if type(age) == int and age > 0:
            self.__age = age
        else:
            raise ValueError('Wrong value for age field. Is must be positive number')

    def __was_born(self):
        print(f'Animal {self.__name} was born')
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


    def info(self):
        return f'NAME: {self.__name}, AGE: {self.__age}, BIRTH YEAR: {2024 - self.__age}'

class Cat(Animal):
    def __init__(self, name,age):
        super().__init__(name, age)

class Dog(Animal):
    def __init__(self, name, age, commands):
        super().__init__(name, age)
        self.__commands = commands

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        return self.__commands

    def info(self):
        return 'Hello from Dog!'

class FightingDog(Dog):
    def __init__(self, name, age, commands, wins):
        super().__init__(name, age, commands)
        self.__wins = wins

    @property
    def wins(self):
        return super().wins()+ f', WINS: {self.__wins}'


cat = Cat('Tom', 5)
dog = Dog('Snoopy', 3, 'Sit')
dog.commands = 'Sit, run'

animals_list= [Cat, Dog, FightingDog]
for animal in animals_list:
    print(Animal.info())
# print(cat.info())
# print(dog.commands)
# print(dog.info())




#
#
# some_animal = Animal('Dura4ok', 3)
# some_animal.set_age(11)
#
# print(some_animal.info())