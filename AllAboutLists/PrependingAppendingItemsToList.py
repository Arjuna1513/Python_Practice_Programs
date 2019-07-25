list1 = [1, 2, 3, 4, 5]
list1 = list1 + [6, 7] #this appends [6, 7] to list1
print(list1)


list2 = [1, 2, 3, 4, 5]
list2 = [-1, 0] + list2 # this prepends [-1, 0] to list2
print(list2)

"""Even though we want to add only one item to list we should specify it as singleton list
else error will be thrown"""

#list2 = list2 + 20 # results in "can only concatenate list (not "int") to list" error
#print(list2)

list2 = list2 + [89]
print(list2)

list2 + [11]
print(list2)

