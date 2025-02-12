from threading import Thread
from time import sleep
import random
from queue import Queue


class Table:  # - стол, хранит информацию о находящемся за ним гостем (Guest)
    def __init__(self, number: int):
        self.number = number
        self.guest = None


class Guest(Thread):  # - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд
    def __init__(self, name: str):
        super().__init__()  # вызов конструктора родительского класса
        self.name = name

    def run(self):  # кафе, в котором есть определённое кол-во столов и происходит имитация
        # прибытия гостей (guest_arrival) и их обслуживания (discuss_guests)
        super().run()
        sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        free_tables = len(self.tables)
        for guest in guests:
            if not free_tables:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
                continue
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            free_tables -= 1

    def discuss_guests(self):
        while any(table.guest is not None for table in self.tables) or not self.queue.empty():
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest.join()
                        if not self.queue.empty():
                            table.guest = self.queue.get()
                            table.guest.start()
                            print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        else:
                            table.guest = None
            sleep(0.1)



if __name__ == '__main__':
    tables = [Table(number) for number in range(1, 6)]
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    guests = [Guest(name) for name in guests_names]
    cafe = Cafe(*tables)
    cafe.guest_arrival(*guests)
    cafe.discuss_guests()