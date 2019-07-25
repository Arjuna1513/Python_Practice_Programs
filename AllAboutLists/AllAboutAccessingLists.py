list1 = [1, 5, 'Arjun', 11, 'Bhishma']

"""for item in list1:
    print(item, end=',\t')
print('\n')

print(list1[len(list1)-1])
print(list1[-2])
print(list1[1:3]) # it prints the value starting from index and till stop index i.e. inclusive of start
# and exclusive of stop index"""

#print(list1[-1]) # print(list1[-1:]) both are same except the second one displays ['Bhishma'] but
# 1st 1 displays only Bhishma

# print(list1[1]) #displays element at 1st index
# print(list1[1:]) # displays all elements including the index mentioned

# print(list1[::]) # prints all the elements in the list

# print(list1[:])  # prints all the elements in the list

# print(list1[:3]) # prints all the elements till the index 3(exclusive of 3)

# print(list1[-2:]) # just works exactly opposite to list1[:2] except that - indicates inclusive of both staet and
# end index

# print(list1[:-2]) # displays all elemets in list that comes after -2 exclusive of -2

# print(list1[:2:]) # displays all the elements that comes before index 2.

# print(list1[:-2:]) # displays all the elements that comes after -2

# print(list1[-5:-3]) # slicing does not work in case of negative values

# print(list1[1:-2])

list2 = [2, 1, 6, 4, 11, 10, 33]
# print(min(list2)) # these won't work when we have str and int values in list

# print(max(list2)) # prints min value present in the list

#print(list2[0:7:0]) # slice step cannot be zero error

#print(list2[0:7:3]) # begins from 0 and till 7th index it will print all the
# elements appear at the 3rd index

#print(list2[::2]) # prints 0th item and then from there prints every 2nd item.

# print(list2[-3:])
# print(list2[:-3])

# print(list2[-5:-3])

# striding with negative values
# print(list2[-1:-8:-2])

# print(list2[::-1]) # this stride reverses the list2 contents

"""list3 = [1, 2, 3]
list4 = list([4, 5, 6])

list5 = list3+list4
print(list5)"""

list1 = list1 * 2
print(list1)




