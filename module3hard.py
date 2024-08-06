data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(len(data_structure))
print(list(data_structure))
sum1 = sum(data_structure[0])
print(sum1)
sum2 = sum(data_structure[1].values())
print(sum2)
print(list(data_structure[2]))
# result = calculate_structure_sum(data_structure)
# print(result)