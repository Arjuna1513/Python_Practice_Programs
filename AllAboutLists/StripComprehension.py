fruits = ['  apple  ', '  bannana', '  mango    ', 'grapes    ']
fruits[:] = [x.strip(' ') for x in fruits]
print(fruits)

squares = [(x, x**2) for x in range(4)]
print(squares)

squares1 = []
for x in range(0, 4):
    squares1.append((x, x**2))

print(squares1)

elements1 = [[x, y] for x in range(4) for y in range(4) if x != y]
print(elements1)