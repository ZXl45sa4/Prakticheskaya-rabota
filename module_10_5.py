import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as f:
        while True:
            # считываем строку
            my_lines = f.readline()
            # прерываем цикл, если строка пустая
            if not my_lines:
                break
            all_data.append(my_lines.strip())
            # закрываем файл
    return all_data


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start = datetime.datetime.now()
    for i in filenames:
        data = read_info(i)
    end = datetime.datetime.now()
    print(f'{end - start} (линейный)')

    # Многопроцессный
    start_1 = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_1 = datetime.datetime.now()
    print(f'{end_1 - start_1} (многопроцессный)')