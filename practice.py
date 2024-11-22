class Car:
    def __init__(self,car_make, model, year):
        self.__car_make = car_make
        self.__model = model
        self.__year = year

    @property
    def car_make(self):
        return self.__car_make

    @car_make.setter
    def car_make(self,value):
        self.__car_make = value

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self,value):
        self.__model = value

    def __str__(self):
        return f'MODEL: {self.__model}, CAR MAKE: {self.__car_make}, YEAR: {self.__year}'

    def start_engine(self):
        print (f'Car {self.__car_make},{self.__model} started engin')

car = Car('X7', 'BMW', 2024)

print(car)

car.start_engine()


class Bank:
    def __init__(self, balance=0):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,value):
        if value >=0:
            self.__balance = value
        else:
            print('Баланс не может быть отрицательным!')

    def manage_balance_(self):
        print(f'Ваш баланс равен: {self.balance}')

        try:
            add_to_balance = float(input("Введите сумму для пополнения баланса:"))
            if add_to_balance > 0:
                self.balance += add_to_balance
                print(f'Ваша баланс равен: {self.balance}')
            else:
                print('Сумма к пополнению не может быть отрицательной')
        except ValueError:
            print('Введите корректное число')

        try:
            remove_from_balance = float(input('Введите сумму для снятия с счета:'))
            if remove_from_balance > 0:
                if self.balance >= remove_from_balance:
                    self.balance -= remove_from_balance
                    print(f'Ваша баланс равен: {self.balance}')
                else:
                    print("Недостаточно средств для снятия")
            else:
                print("Сумма для снятия должнга быть положительной")
        except ValueError:
            print('Введите корректное число!')

bank = Bank()
bank.manage_balance_()

