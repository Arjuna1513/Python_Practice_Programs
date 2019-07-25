"""elements = [1, 9, 'bat', 'ball', 99, 10]
print(elements)

elements[2] = 999;
print(elements) # bat is replcaed with 999"""

"""val = 'Arjuna'
val[2]=9
print(val)""" #throws error 'str' object does not support item assignment because strings are immutable

"""del elements[3] # del removes the value based on index value unlike where remove deletes based on value mentioned.
print(elements)

elements.__delitem__(2) # similar to del elements[2]
print(elements)
"""

elements1 = [10, 20, 'aaa', 88, 'bbb', 33, 41, 'xxx']

elements1[2] = [11, 21]
print(elements1)

elements1[1:3] = ['a', 'b']
print(elements1)