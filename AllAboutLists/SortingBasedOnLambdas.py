"""list1 = [('arjuna', 22), ('bhishma', 33), ('nakula', 20), ('sahadeva', 19)]
# let's sort tuples based on lambdas
list1.sort(key=lambda x: x[0])
for item in list1:
    print(item)
    """

"""lambda functions are nameless functions which are used for a time being usually when a separate method
is not required i.e. when we want some evaluation that is to be done in the function

It takes one or multiple arguments and there will eb only one expression
in the above function x is the argument i.e. tuple is the argument and it evaluates to x[0] i.e.
returns tuple[0]
"""

list2 = [1, 2, 3, 4, 5, 6]
"""for i in range(list2.__len__()):
    list2[i] = list2[i] * 2"""


for i in range(list2.__len__()):
    value = lambda x: x * 2
    list2[i] = value(list2[i])
    print(type(value))
"""In the above type(value) returns as a function so value is a function as well so to get the value of 
expression returned by lambda just pass the parameter as shown above list2[i] = value(list2[i])"""

for item in list2:
    print(item)

