class Car:
    def __init__(self, model, year):
        self.__model = model
        self.__year = year

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    def drive(self):
        print(f'Car {self.__model} is driving.')

    def __str__(self):
        return f'MODEL: {self.__model}\nYEAR: {self.__year}'

    def __lt__(self, other):
        return  self.__year < other.__year

    def __gt__(self, other):
        return self.__year > other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year
    def __le__(self, other):
        return self.__year <= other.__year

    def __ge__(self, other):
        return self.__year >= other.__year

class FuelCar(Car):
    total_fuel = 0

    def __init__(self,model,year, fuel_bank):
        # super(FuelCar, self).__init__(model, year)
        # super().__init__(model, year)
        Car.__init__(self,model, year)
        self.__fuel_bank = fuel_bank


    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by fuel.')

    def __str__(self):
        return super().__str__() + f'\nFuel Bank: {self.__fuel_bank}'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank

class ElectricCar(Car):
    def __init__(self, model,year,battery):
        Car.__init__(self,model,year)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self,value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.__model} is driving by Battery.')

    def __str__(self):
        return super().__str__() + f'Battery: {self.__battery}'

class HybridCar(FuelCar, ElectricCar):
    def __init__(self,model, year,battery,fuel_bank):
        FuelCar.__init__(self,model,year,fuel_bank)
        ElectricCar.__init__(self,battery)





fuel_car = FuelCar('Audi A8', 2020, 75)
# print(fuel_car)

number1 = 2
number2 = 10
print(f'Number one is smaller then number two: {number1 < number2}')





# some_car = Car('Audi', 2000)
#
# print(some_car)

