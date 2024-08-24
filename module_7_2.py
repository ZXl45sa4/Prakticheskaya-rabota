def custom_write(file_name, strings):
    f = open(file_name, 'w+',  encoding='utf 8')
    strings_positions ={}
    for i in strings:
        f.write(i + '\n')
        strings_positions[(len(strings_positions) + 1, f.tell())] = i
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
