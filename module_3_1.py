calls = 0

def count_calls():
    global calls                                                            # подсчитывающая вызовы остальных функций
    calls+=1

def string_info(string):                                                    # Функция string_info
    count_calls()
    lowercase = string.lower()                                              # строка в нижнем регистре
    uppercase = string.upper()                                              # строка в верхнем регистре
    argument = (len(string), uppercase, lowercase)
    return argument

def is_contains(string, list_to_search):                                    # принимает два аргумента: строку и список
    count_calls()
    lowercase = string.lower()
    if lowercase in (i.lower() for i in list_to_search):
        return True                                                         #True, если строка находится в этом списке
    else:
        return False                                                         #False - если отсутствует
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))      # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))        # No matches
print(calls)