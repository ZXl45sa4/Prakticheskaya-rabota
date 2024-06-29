my_list = [42, 69, 322, 0, 99, -5, 9, 8, 7, -6, 5]
nach_znach = 0
while nach_znach < len(my_list):
    if my_list[nach_znach] >= 1:
        print(my_list[nach_znach])
        nach_znach += 1
        continue
    elif my_list[nach_znach] >= 0:
         nach_znach += 1
    else:
        break