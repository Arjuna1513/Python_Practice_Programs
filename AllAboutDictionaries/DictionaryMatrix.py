dict1 = {x:x**2 for x in range(3)}

print(dict1)

dict2 = {x:{x:x*2 for x in range(4)} for x in range(4)}

for x,y in dict2.items():
    print(x,y)
    for _ in dict(y).items():
        print(_)
        for item in range(len(_)):
            print(item, end='\t')
        print()
    print()

# since dictionaries cannot be indexed using integers it is not possible to construct
# nested dictionaries using nested for loops.

