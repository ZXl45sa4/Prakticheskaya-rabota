#Lambda-функция:

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(list(result))

#Замыкание:
def get_advanced_writer(file_name):
    f = open(file_name, 'w+', encoding='utf 8')
    def write_everything(*data_set):
        for i in data_set:
            f.write(str(i) + '\n')
        return
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Метод __call__:

from random import choice
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())