name = int(input("vvod na konsol'name:"))
second = int(input("vvod na konsol'second:"))
third = int(input("vvod na konsol'third:"))
if name==second==third:
    print('(3)'+':','числа равны')
elif name==second or second==third or third==name:
    print('(2)'+':','2 из 3 введённых чисел равны между собой')
# elif name==second!=third:
#     print(name,'=',second,'≠',third)
#     print(2)
# elif name!=second==third:
#     print(name,'≠',second,'=',third)
#     print(4)
# elif name==third!=second:
#     print(name,'≠',third,'=',second)
#     print(6)
else:
    print('(0)'+':','числа не равны')
