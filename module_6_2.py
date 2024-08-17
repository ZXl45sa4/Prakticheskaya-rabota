class Vehicle: #любой транспорт
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, model, color, engine_power):
        self.owner = str(owner)  #владелец транспорта. (владелец может меняться)
        self.__model = str(model)  #модель (марка) транспорта. (мы не можем менять название модели)
        self.__color = str(color)  #название цвета. (мы не можем менять цвет автомобиля своими руками)
        self.__engine_power = int(engine_power)  #мощность двигателя. (мы не можем менять мощность двигателя
        # самостоятельно)

    def get_model(self): # возвращает строку: "Модель: <название модели транспорта>"
        return self.__model

    def get_horsepower(self): # возвращает строку: "Мощность двигателя: <мощность>"
        return self.__engine_power
    """
    Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в списке 
    __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
    """
    def get_color(self):
        return  self.__color

    def set_color(self,new_color): # название цвета. (мы не можем менять цвет автомобиля своими руками).
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

    def print_info(self):
        print(f'Модель:{self.get_model()}')
        print(f'Мощность двигателя:{self.get_horsepower()}')
        print(f'Цвет:{self.get_color()}')
        print(f'Владелец:{ self.owner}')

class Sedan(Vehicle): #(седан) - наследник класса Vehicle
    __PASSENGERS_LIMIT = 5 #(в седан может поместиться только 5 пассажиров)

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
