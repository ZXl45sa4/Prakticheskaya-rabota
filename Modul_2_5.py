def get_matrix(n, m, value):                    # Функцию get_matrix с параметрами n, m и value
    matrix = []                                 # Пустой список matrix внутри функции get_matrix
    for i in range(n):                          # Первый(внешний) цикл for для кол-ва строк матрицы, n повторов
        spisok = list()                         # Пустой список
        matrix.append(spisok)                   # Добавление пустого списка в список matrix
        for j in range(m):                      # Второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов
            spisok.append(value)                # Добавление в ранее добавленный пустой список значениями value.
    return matrix                               # Возвращение к matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)