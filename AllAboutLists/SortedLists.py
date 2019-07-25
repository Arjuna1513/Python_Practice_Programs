"""list1 = [11, 22, 1, 5, 99, 33, 29]

sorted(list1)

for item in list1:
    print(item, end='\t')
    the above did not print sorted list because when sorted method is used it will sort the items present in a
    list and puts that in to a new list i.e. it creates new list and puts the sorted elements hence the 
    above for loop prints the unsorted elements. to overcome this when sorted is used assign it to a list1


print('\n\n')
list1 = sorted(list1)
for item in list1:
    print(item, end='\t')
    Here the returned value of sorted list is reassigned to list1 hence the list1 has sorted items

print('\n\n')

list1 = sorted(list1, reverse=True)
for item in list1:
    print(item, end='\t')
# the above one sorts the list in reverse order
"""

list2 = [('Arjuna', 33), ('Bhishma', 29), ('Sahadeva', 19), ('Nakula', 23)]
list2 = sorted(list2, key=lambda x: x[0], reverse=False)
for item in list2:
    print(item, end='\t')



