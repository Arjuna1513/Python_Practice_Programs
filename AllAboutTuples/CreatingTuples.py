"""tuple1 = (1, 2, 3, 4, 5)
for item in tuple1:
    print(item, end='\t')
print('\n')

# create nested tuple
tuple2 = (1, 2, (2, 3, (4, 5)), 6, 7, 8)
print(tuple2[0])
print(tuple2[1])
print(tuple2[2])
print(tuple2[2][2][0])
print(tuple2[2][2][1])
"""


# enter values in tuple using comprehension
"""tuple3 = (x*2 for x in range(5))
for item in tuple3:
    print(item)
"""

"""
tuple4 = ((x, x*2) for x in range(4))
for item in tuple4:
    print(item)
"""

"""
tuple5 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2)
print(tuple5.count(2))

print(tuple5.__len__())

print(tuple5.index(3))

print(tuple5.index(2, 4, 11))
# will search for the value 2 starting from 4th index till 11 index(exclusive)

print(tuple5.__contains__(10))
# returns true if the tuple contains the given value

tuple6 = (1, 2, 3, 4, 5, 6, 7,  9, 10, 2)
print(tuple5.__eq__(tuple6))
# returns true if both the tuples are same else returns false.

print(tuple5.__sizeof__())
# returns the size memory occupied by tuple
"""

tuple5 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2)
tuple5 = tuple5.__add__((99,))
print(tuple5)
# here we can get a question that how can we able to add value to tuple when it is immutable
# here when we add/concatenate a new tuple is being created with added value.

print(tuple5.__getitem__(5))
# it gets the item present at the mentioned index.


"""
list1 = [1, 2, 3, 4]
s1, s2, s3, s4 = list1
print(s1, s2, s3, s4)

list2 = [((y, y*2) for y in range(4)) for x in range(4)]
for row in list2:
    for col in row:
        print(col, end='\t')
    print('\n')

for item in list2:
    print(item)
"""

tuple1 = (1, 2, 3, 4, 5)
tuple1.__add__((99,))
print(tuple1)

