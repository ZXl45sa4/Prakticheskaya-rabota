def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result % 2 != 0 or result == 2:
            print(f'Простое')
        else:
            print(f'Составное')
        return result
    return wrapper


@is_prime
def sum_three(*args):
    total = sum(args)
    return total


result = sum_three(2, 3, 6)
print(result)