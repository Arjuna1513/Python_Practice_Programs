"""
append(object)  --> appends object to the end of the list

list1 = list1 + [1,2,3] --> Here when + is used all the elements from [1, 2, 3] are broken and then appended to list1
                            individually.


"""

"""
Append and extend examples:
list1 = [1, 2, 3, 4]
list1.append([5])
print(list1)

# ** output --> [1, 2, 3, 4, [5]] ** #

list2 = [1, 2, 3, 4]
#list2.extend(99)
#print(list2)

# ** output --> 'int' object is not iterable ** # because it accepts only iterable object

list2.extend('abc')
print(list2)

# ** output --> ecen strings are also iterable but when added each caharcter in string is added invidually
# [1, 2, 3, 4, 'a', 'b', 'c']

list3 = [1, 2, 3, 4]
list3.extend([5, 6])
print(list3)

# ** output --> it doesn't just append the added list to original list but also it breakes the arhument list
# in to individual values and appends it to the end of the list
# output     [1, 2, 3, 4, 5, 6]

"""

"""list4 = [1, 2, 3, 4, 5, 6]
list4.pop()
print(list4)
# pop without argument removes the last element from the list

list4.pop(-2)
print(list4)
# pop accepts index of only negative values

list4.pop(-10)
print(list4)
# if index is out of range then an error is thrown
"""

list5 = [1, 2, 3]
s1, s2, s3 = list5
print(s1, s2, s3)