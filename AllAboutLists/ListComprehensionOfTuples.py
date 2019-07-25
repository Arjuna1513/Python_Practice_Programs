

"""for row in elements:
    for col in row:
        print(col, end='\t')
    print('\n')

print(elements[0][0]) # u cannot try to view the tuple present in list if u try it will throw
# "TypeError: 'generator' object is not subscriptable" error.

tuple1=((1, 2), (3, 4))
print(tuple1[0][0])"""

elements = [x for x in range(5)]
print(elements)

del elements[2]
print(elements)

#del elements
print(elements)

tuple1 = (1, 2, 3, 4, 5)
del tuple[1] # tuple doesn't support deletion of items.

