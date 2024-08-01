
def test_function(): #Создайте новую функцию def test_function
    print(str('"Я в области видимости функции test_function"'))
    def inner_function(): #Создайте другую функцию внутри функции inner_function
        print(str('"Я в области видимости функции inner_function"'))
    inner_function()

test_function() # здесь работает
inner_function() #Traceback (most recent call last):
#   File "C:\GitProject\pythonProjectModule_4_2\.venv\module_4_2.py", line 9, in <module>
#     inner_function()
#     ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?


