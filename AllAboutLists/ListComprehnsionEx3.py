elements = [0, 1, 2, 3, 4, 5, 6]
elements = [x*2 for x in elements]
print(elements)

for x in range(elements.__len__()):
    elements[x] = elements[x]*2

print(elements)

#after executing [x*2 for x in elements] stmt assign the result to elements again becoz the stmt creates
# new list object