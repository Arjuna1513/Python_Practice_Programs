dict1 = {1:2, 3:4, 'a':'b', 5:{1:2}}
# print(dict1)
#
# print(len(dict1)) # prints length of dict1
#
# print(dict1.items()) # Returns a list of items with both key and value pairs and since the list is
# # returned we are able to iterate over it
#
# print(dict1.values()) # returns only list of values
#
# print(dict1.keys()) # returns list of keys
#
# print(dict1.get('a')) # returns value associated with key, if not found none is returned.
#
# print(dict1.copy()) # returns a copy of the dictionary
#
# dict2 = dict1.copy()
# print(dict2)

# print(dict1.popitem()) # popitem removes the last element
# print(dict1)

# print(dict1.pop('a')) # deletes the key, value pair of mentioned key
# print(dict1)

print(dict1.__getitem__('a')) # returns the value of key 'a'

print(dict1.__contains__('a')) # returns true if 'a' key is present else returns false

print(dict1.__delitem__('a')) # deleted the given item but wont return the deleted item.