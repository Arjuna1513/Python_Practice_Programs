list1 = [1, 5, 4, 9, 11, 33, 24, 56, 34]

"""print("Elements sorted")
list1.sort()
for item in list1:
    print(item)"""

"""print("Elements sorted in reverse order")
list1.sort(reverse=True)
for item in list1:
    print(item)"""

"""Sometimes we want to sort the tuples present in list based on second value of tuple so int
that case define a custom function to do that"""


def custom_sort(t):
    return t[1]
# if u return the tuple index value which is not present u will end up getting
# tuple index out of range error


list2 = [(11, 22), (22, 44), (41, 50), (77, 1)]
print("sorting elements of tuples present in list in ascending based on second item ")
list2.sort(key=custom_sort, reverse=False)
for item in list2:
    print(item)

"""How does above one worked?
first we have defined an custom_sort(t) method and it returns the index value of the
tuple using which the sort has to be done.
so when the sort method is called we have given key = custom_sort and the custom sort 
returned the value 0 which means sort has to be done based on first index value of sort"""



