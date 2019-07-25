dict1 = {
            1:2,
            'a':{1:2, 3:4, 'x':'y'},
            'c':'d', 4:5,
            5:{11:22, 33:44, 44:55}
        }
# the above one is nested dictionary
# for key, value in dict1.items():
#     print(key, '=', value)

# manually accessing the values of nested dictionaries

print(dict1[1])
print(dict1['a'])
print(dict1['a'][1])
print(dict1[5][33])