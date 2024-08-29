import time
import os.path
'''
                Создайте новый проект или продолжите работу в текущем проекте.
1. Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
2. Примените os.path.join для формирования полного пути к файлам.
3. Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
4. Используйте os.path.getsize для получения размера файла.
5. Используйте os.path.dirname для получения родительской директории файла.
'''

print('Текущая директория:', os.getcwd())
#print(os.listdir())
file = [f for f in os.listdir() if os.path.isfile(f)]
print(file)
print(os.stat(file[2]))

path = os.getcwd()

for root, dirs, files in os.walk(path):
    for file in files:
        filepath = os.path.join(path)
        filetime = os.path.getmtime(path)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(path)
        parent_dir = os.path.dirname(path)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: '
              f'{formatted_time}, Родительская директория: {parent_dir}')