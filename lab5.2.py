# Given lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]


result = list(map(lambda x, y, z: x + y + z, list1, list2, list3))

print(result)

