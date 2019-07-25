# create a matrix with nested lists using comprehensions

"""elements = [[x for x in range(4)]for row in range(4)]
for row in elements:
    print(row)"""

# Create a 4*4 matrix without using
"""elements = []
for row in range(4):
    inner_list = []
    for col in range(4):
        inner_list.append(col)
    elements.append(inner_list)

for row in elements:
    print(row)"""

# Creating 4 * 4  deep nested matrix using comprehension:
elements = [[[z for z in range(2)]for y in range(4)]for x in range(4)]
for row in elements:
    print(row)

# Creating 4 * 4  deep nested matrix without using comprehension:

"""elements = []
for x in range(4):
    inner_list = []
    for y in range(4):
        deep_list = []
        for z in range(2):
            deep_list.append(z)
        inner_list.append(deep_list)
    elements.append(inner_list)

for row in elements:
    print(row)"""

# Transpose of 3*4 matrix using Comprehension

"""elements = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
           ]

elements = [[row[i] for row in elements]for i in range(4)]
for row in elements:
    print(row)"""

# Transpose of 3*4 matrix without using Comprehension
"""elements = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
           ]
transposed_list = []
for x in range(4):
    inner_list = []
    for row in elements:
        inner_list.append(row[x])
    transposed_list.append(inner_list)

for row in transposed_list:
    print(row)"""






