class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
class Car:
    def __init__(self, model, vin_number, numbers):
        self.model = model
        self.__vin = vin_number
        self.__numbers = numbers
        if self.__is_valid_vin(vin_number) == True:
            self.__vin = vin_number
        if self.__is_valid_numbers(numbers) == True:
            self.__numbers = numbers

    def __is_valid_vin(self, __vin):
        if not isinstance(__vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not 1000000 <= __vin <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, __numbers):
        if not isinstance(__numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if __numbers != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')




