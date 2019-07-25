fruits = ['apple', 'banana', 'citrus', 'orange', 'grape', 'apple', 'banana', 'banana']

print("Lets print the size of the list = ", len(fruits))

print("lets pop the item and print it = ", fruits.pop())
#pop() method removes and returns the removed value.

print("Lets remove the item and print it = ", fruits.remove('apple'))
#remove method removes the element but will not return the removed item.

fruits.remove('banana')
#remove takes only 1 argument and it removes only the first occurance of the given element, not all occurances

print("Lets print all values from the list\n")
for fruit in fruits:
    print(fruit)

print("Total number of bananas present are ", fruits.count('bananaa'))
# it returns the total occurances of given value present in list, if none returns 0 but will not throw any error.

fruits.append("berry")
# adds the item at the end of the list and returns the value added.

fruits.insert(1, 'muskmelon')
# inserts the value given at the specific index and the old value at the index will be pushed to next index.

for items in fruits:
    print(items, '\n\n')

fruits.append('apple')
fruits.append('banana')

for items in fruits:
    print(items)

print("index of value banana is = ", fruits.index('banana'))
# the above one returns the index of first occurance of given value

print("index of value banana from specific index is  = ", fruits.index('banana', 5, 10))
""" the above one returns the index of first occurance of given value starting from index 5(inclusive) i.e even
if the element is present at the start point mentioned it will display that element.
If u give the stop index greater than start index u will get "ValueError: 'banana' is not in list" error.

If u give the stop index same as start index u will get "ValueError: 'banana' is not in list" error.
"""

fruits.sort()
print("values of sorted list are as follows\n")
for item in fruits:
    print(item)

fruits.reverse()
print("values of list in reverse order\n")
for item in fruits:
    print(item)

print(fruits.__contains__('citrus'))
# returns true if given element is present else returns false.



