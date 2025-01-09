import threading
import time
import random


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):  # пополнение
        for i in range(100):
            popolnenie: int = random.randint(50, 500)
            self.balance += popolnenie
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение:{popolnenie}. Баланс:{self.balance}')
            time.sleep(0.001)

    def take(self):  # снятие
        for i in range(100):
            snatie = random.randint(50, 500)
            print(f'Запрос:{snatie}')
            if snatie <= self.balance:
                self.balance -= snatie
                print(f'Снятие:{snatie}. Баланс:{self.balance}')
            time.sleep(0.001)

            if snatie > self.balance:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
