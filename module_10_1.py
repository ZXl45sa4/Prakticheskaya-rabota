import threading
from time import sleep
from datetime import datetime
time_start = datetime.now()
def write_words(word_count, file_name):
    with open(file_name, 'wt', encoding='utf-8') as inFile:
        for i in range(1, word_count + 1):
            inFile.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start

print(time_res)

time_start = datetime.now()

# Создание потока
potok_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
potok_2 = threading.Thread(target=write_words, args=(200, 'example6.txt'))
potok_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
potok_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

# Запуск потока
potok_1.start()
potok_2.start()
potok_3.start()
potok_4.start()

# Ожидание завершения потока
potok_1.join()
potok_2.join()
potok_3.join()
potok_4.join()

time_end = datetime.now()
time_res = time_end - time_start
print(time_res)

