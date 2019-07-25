"""eles = [-9, -5, 5, 4, 3, -2]
eles = [x for x in eles if x >= 0]
print(eles)"""

#similarly

"""eles1 = [-9, -5, -9, 4, 3, -2]
print(len(eles1))
print(eles1)
for i in eles1:
    if i < 0:
        eles1.remove(i)

print(eles1)"""

eles5 = [1, 4, 6, 7, 9]
for x in eles5[:]:
    if x % 2 != 0:
        print(x)
        eles5.remove(x)
print(eles5)
#basically removing items from list while iterating is not supported in python so use comprehensions
"""
eles5 = [1, 4, 6, 7, 9]
for x in eles5[:]:
    if x % 2 != 0:
        print(x)
        eles5.remove(x)
print(eles5)
the above code worked perfectly fine becoz we are deleting the
contents of the original list by mentioning that using for x in eles5[:]: where as below leads to improper results:

eles5 = [1, 4, 6, 7, 9]
for x in eles5:
    if x % 2 != 0:
        print(x)
        eles5.remove(x)
print(eles5)
"""

eles6 = [1, 4, 6, 7, 9]
eles6[:] = [x for x in eles6 if x % 2 == 0]
print(eles6)
#print(eles7)