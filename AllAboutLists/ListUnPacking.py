list1 = [[1,2,3], [4,5,6], [7,8,9]]

for x,y,z in list1:
    print(x,y,z)

"""
Here the list has nested lists with each containing 3 values so in order to access 3 values at a time
from for loop use a unpacking technique

above is the example.
But make sure that all the nested lists has the same number of values i.e. if 1st list has
3 values rest of the lists should also have 3 values else not enough values error will be thrown.
"""

list2 = [[[x**2 for x in range(3)]for x in range(4)]for x in range(4)]

# for item in list2:
#     print(item)