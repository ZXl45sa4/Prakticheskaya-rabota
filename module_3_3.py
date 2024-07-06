print('1. Функция с параметрами по умолчанию:')

def print_params(a = 1, b = 'Строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

print()
print('2. Распаковка параметров:')

values_list = [1, False, 'Строка']                                # Список
values_dict = {'a' : 6, 'b' : [1, 2], 'c' : (1, 2, 3)}            # Словарь

print_params(*values_list)
print_params(**values_dict)

print()
print('3. Распаковка + отдельные параметры:')

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
