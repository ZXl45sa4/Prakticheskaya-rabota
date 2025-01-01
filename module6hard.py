import math


class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=bool):
        self.__sides = [sides for _ in range(self.sides_count)]
        self.__color = list(color)
        self.filled = filled

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    @staticmethod
    def __is_valid_color(r, g, b):
        return True if 0 < r < 255 and 0 < g < 255 and 0 < b < 255 else False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.__color = [r, g, b]

    def set_sides(self, *args):
        my_list = [*args]
        if self.__is_valid_sides(my_list) is True:
            self.__sides = my_list

    def __is_valid_sides(self, my_list):
        if len(my_list) == self.sides_count:
            for i in my_list:
                if i < 0:
                    return False
            return True
        else:
            return False

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color=color, sides=sides)
        self.__radius = sides / 2 * math.pi
        self.__square = 0

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color=color, sides=sides)
        self.__sides = sides
        self.__height = 0
        self.__square = 0
        self.__semiperimeter = sum(sides) / 2
        self.__a = self.__sides[0]
        self.__b = self.__sides[1]
        self.__c = self.__sides[2]

    def get_height(self, side):
        if side == "a":
            side = 2 * self.get_square() / self.__a
        elif side == "b":
            side = 2 * self.get_square() / self.__b
        elif side == "c":
            side = 2 * self.get_square() / self.__c
        return side

    def get_square(self):
        self.__square = (self.__semiperimeter * (self.__semiperimeter - self.__a)
                         * (self.__semiperimeter - self.__b)
                         * (self.__semiperimeter - self.__c)) ** 0.5
        return self.__square


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(sides=sides, color=color)
        self.__sides = sides

    def get_volume(self):
        return self.__sides ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())


# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
