"""tuple1 = tuple(x for x in range(4))
for item in tuple1:
    print(item)"""

tuple2 = tuple((y for y in range(4)) for x in range(4))
for row in tuple2:
    for col in row:
        print(col, end ='\t')
    print('\n')

tuple3 = tuple(((y, y*2) for y in range(4))for x in range(4))
for row in tuple3:
    for col in row:
        print(col, end='\t')
    print('\n')