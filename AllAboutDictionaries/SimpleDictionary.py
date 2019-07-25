dict1 = {1:2, 2:'Arjuna', 'age':33, 'status':'Engineer'}

"""print(dict1[1])
print(dict1[2])
print(dict1['age'])
print(dict1['status'])"""
# print(dict1['address']) # throws key error b'coz address key is not in dict1.

#print(dict1.get('address'))
# get method also returns value but the difference is it will not thorw error but returns as None
# when key is not found.

# accessing values from dict1
"""for key, value in dict1.items():
    print(key, value)"""
# the above one will return both key and value pair.


# for key in dict1:
#     print(key)

# The above one will return only keys, not values.

for value in dict1.items():
    print(value)

"""# The above will display the key, value pair in the form of tuples
e.x.  (1, 2)
(2, 'Arjuna')
('age', 33)
('status', 'Engineer')"""

"""
print(dict1.keys()) # it returns a list of keys
keys = dict1.keys()
for x in keys:
    print(x) # and a list can be iterated using for loop.
"""

# print(dict1.values()) # it returns a list of values.

# list1 = list(dict1)
# print(list1)  # if u try to convert dict ti list then only keys will be added to list, not values.




