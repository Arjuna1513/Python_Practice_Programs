# Using Comprenhension

"""elements = [[0 for col in range(3)] for row in range(4)]

for row in elements:
    print(row)"""

# Without using comprehensions

"""elements = []
for row in range(4):
    inner_list = []
    for col in range(3):
        inner_list.append(col)
    elements.append(inner_list)

for row in elements:
    print(row)
    """

# Creating nested lists
"""elements = [[[v for v in range(2)]for v in range(3)] for row in range(3)]

# for item in elements:
print(elements)"""

# Achieving the above without using comprehensions
elements = []
for x in range(3):
    inner_list = []
    for y in range(3):
        innermost_list = []
        for z in range(2):
            innermost_list.append(z)
        inner_list.append(innermost_list)
    elements.append(inner_list)

for item in elements:
    print(item)





