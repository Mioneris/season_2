class Transport:
    def __init__(self, the_model, the_year, the_color):
        self.model = the_model
        self.year = the_year
        self.color = the_color


class Plane(Transport):
    def __init__(self,the_model, the_year, the_color ):
        super().__init__(the_model, the_year, the_color)


class Car:
    #constructor                 parameters
    def __init__(self, the_model, the_year, the_color, penalties=0):
        #fileds / attributes
        self.model = the_model
        self.year = the_year
        self.color = the_color
        self.penalties = penalties


class Truck(Car):
    def __init__(self, the_model, the_year, the_color, penalties=0, load_capacity=0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capacity= load_capacity

        def load_cargo(self, weight, product_type):
            if weight > self.load_capacity:
                print(f'You cant load mire than {self.load_capacity}kg ')
            else:
                print(f'You successfully loaded the cargo of {product_type} ({weight}kg) ')

truck = Truck('Volvo', 2020,'Black', 500, 30000 )
print(f'Model:{truck.model}')

    # #method
    # def drive(self,city):
    #     print(f'Car {self.model} is driving to {city}')



my_car = Car('BMW X6', 2020, 'Black')
print(my_car)
print(f'MODEL: {my_car.model}\nYEAR: {my_car.year}\nCOLOR: {my_car.color}\nPEN:{my_car.penalties}\n')

best_car = Car(penalties=900,the_year=2021, the_model='Honda Fit', the_color='Blue')
print(f'MODEL: {best_car.model}\nYEAR: {best_car.year}\nCOLOR: {best_car.color}\n')

best_car.color = 'Red'
print(f'MODEL: {best_car.model}\nYEAR: {best_car.year}\nNEW COLOR: {best_car.color}')

