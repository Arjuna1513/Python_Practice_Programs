# def one():
#     return "January"
#
# def two():
#     return "February"
#
# def three():
#     return "March"
#
# def four():
#     return "April"
#
# def five():
#     return "May"
#
# def six():
#     return "June"
#
# def seven():
#     return "July"
#
# def eight():
#     return "August"
#
# def nine():
#     return "September"
#
# def ten():
#     return "October"
#
# def eleven():
#     return "November"
#
# def twelve():
#     return "December"
#
#
# def intToMonth(argument):
#
#     switcher = {
#                     1:one,
#                     2:two,
#                     3:three,
#                     4:four,
#                     5:five,
#                     6:six,
#                     7:seven,
#                     8:eight,
#                     9:nine,
#                     10:ten,
#                     11:eleven,
#                     12:twelve
#                }
#     # print(f"Month value is {switcher.get(argument, 'Invalid Month number')}")
#     return switcher.get(argument, 'Invalid Month number')
# option = int(input("Enter integer input here>>>"))
# if type(option) != int or option < 0 or option > 12:
#     print("Enter integer number that is greater than 0 and less than 12")
#
# else:
#     month = intToMonth(option)
#     print(month)
#
#
# """
# In python there is no switch statement hence that is compensated using dictionary in python.
#
# switcher is a dictionary defined where we have mapped the values from 1:12 and put that dictionary in method.
#
# Now after the dictionary definition we have called the dictionary using get method using the argument passed to method
#
# and printing the value...
# """

dict1 = {1:2}
dict1.__setitem__(99, 100)
print(dict1)

list1 = [1,2]
list2 = [3, 4]
list1 = list1.__add__(list2)
print(list1.__getitem__(3))

tuple1 = (1 ,2, 3, 4, 5, 6)
print(tuple1.__getitem__(5))

