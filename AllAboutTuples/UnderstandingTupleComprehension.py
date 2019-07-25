x = (x**2 for x in range(4))
print(x)

list1 = list(x)
print(list1)

list2 = [1, 2, 3, (1, 2), 6, (7, 8, (9, 10, (11, 12)))]
print(list2)
print(list2[5][2][2][1])

list3 = [((y, y**2) for y in range(4)) for x in range(4)]
print(list3)