# def add(n1, n2):
#     return n1 + n2
#
# sum = add(11, 22)
# print(f"sum of numbers = {sum}")


# def add(n1, n2):
#     return n1 + n2
#
# sum = add()
# print(f"sum of numbers = {sum}")
# #The above results in "TypeError: add() missing 2 required positional arguments: 'n1' and 'n2'"


# def add(n1=99, n2=1):
#     return n1 + n2
#
# sum = add()
# print(f"sum of numbers = {sum}")
# # The above one works perfectly fine, b'coz even though we have not passed values the method has default values
# # assigned hence it works


# def add(n1=99, n2=10):
#     return n1 + n2
#
# sum = add(n1 = 1, n2 = 2)
# print(f"sum of numbers = {sum}")
# # even though the method has default values 99 and 1 the values passed will override those 99 and 1 with 1 and 2
# # hence the output is 3.



# def add(n1=99, n2=1):
#     return n1 + n2
#
# sum = add(11, 22)
# print(f"sum of numbers = {sum}")
# # similar to above one but this also works, output is 33



# def add(n1=2, n2=5):
#     return n1 + n2
#
# sum = add(n2=99, n1=1)
# print(f"sum of numbers = {sum}")
# # positions of the parameters can be changed and still it works and the output is 100.



# def add(n1, n2):
#     return n1 + n2
#
# sum = add(99, n2=5)
# print(f"sum of numbers = {sum}")
# # even this works

# def add(n1, n2=8):
#     return n1 + n2
#
# sum = add(n1=2, 7)
# print(f"sum of numbers = {sum}")
# # but this won't work