def custom_write(file_name, strings):
    string_position = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings, start=1):
            start_byte = file.tell()
            print(start_byte)
            file.write(string + '\n')
            string_position[(line_number, start_byte)] = string
    return string_position
