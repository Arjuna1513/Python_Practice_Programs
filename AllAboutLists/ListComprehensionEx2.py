squares = [x**2 for x in range(7)]
print(squares)

#OR
def evaluate(x):
    return x ** 2


squares1 = list(map(evaluate, range(10)))
print(squares1)
#print(type(squares))

#if we do not type cast the map to list we will get a map object from map and we' ll not be bale to access
# values of list

squares2 = list(map(lambda x: x**2, range(10)))
print(squares2)


