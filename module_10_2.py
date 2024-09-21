from threading import Thread
from time import sleep
class Knight(Thread):
    def __init__(self, name:str, power:int):
        super().__init__()
        self.name = name
        self.power = power
        self.vrag = int(100)


    def run(self):
        print(f'{self.name}, на нас напали!')
        i = 0
        while i < 10:
            sleep(1)
            i += 1
            self.vrag -= self.power
            print(f'{self.name} сражается {i} день(дня)..., осталось {self.vrag} воинов.' + '\n')
            if self.vrag <= 0:
                self.vrag = 0
                print(f'{self.name} одержал победу спустя {i} дней(дня)!'+ '\n')
                break
        if i == 10:
            print('Битва закончилась!')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
