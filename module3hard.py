def example_function(*args):
    summa = 0
    for cycle in args:
        if isinstance(cycle, dict):
            for key, value in cycle.items():
                summa += example_function(key)
                summa += example_function(value)
        elif isinstance(cycle, list | tuple | set):
            for i in cycle:
                summa += example_function(i)
        elif isinstance(cycle, int | float):
            summa += cycle
        elif isinstance(cycle, str):
            summa += len(cycle)
    return summa


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(example_function(*data_structure))
