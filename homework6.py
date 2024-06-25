my_dict={'Aleksey':1985,'Vladimir': 1990,'Sergei':1986}
print(my_dict)
print(my_dict.get('Vladimir'))
print(my_dict.get('Yulya'))
my_dict.update({'Max':2000,
                'Artem':2000})
print(my_dict)
#____________________________________________________#
my_set={1,1,5,8,3,4,5,9,7,2,9,1,8,5,4,4,6, 'Str', True, False, (4,5,6,1)}
print(my_set)
print(my_set.update([10,11]))
print(my_set)
print((my_set.remove(7)))
print(my_set)