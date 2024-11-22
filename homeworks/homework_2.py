class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_lenght = side_length

    def calculate_area(self):
        return self.__side_lenght ** 2

    def info(self):
        area = self.calculate_area()
        unit = self.unit
        return f'Square side length:{self.__side_lenght}{unit}\n' \
               f'Area: {area}{unit}\n'

class Rectangle(Figure):
    def __init__(self, length,width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__width * self.__length

    def info(self):
        area = self.calculate_area()
        unit = self.unit
        return f'Rectangle length: {self.__length}{unit}\n' \
               f'width: {self.__width}{unit}\n' \
               f'area: {area}{unit}\n'

figures = [Square(5), Square(10),
           Rectangle(12,10), Rectangle(24,5),
           Rectangle(7,8)]

for figure in figures:
    print(figure.info())



# square = Square(5)
# print(square.info())
#
# ractangle = Rectangle(10,5)
# print(ractangle.info())