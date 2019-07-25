from MainPackage import add

if __name__ == '__main__':
    print("Math.py is run directly")
else:
    print("Math.py is run in-directly")

result = add.addMethod(11, 33)
print(f"Result of add operation is : {result}")


"""
Here we are directly running the file Math.py hence __name__ is set to __main__ hence prints Math.py is run directly.
where as add.py is imported and in this file and then it's method add addMethod is called, so add.py file has been called indirectly
hence add.py is run indirectly is printed...
"""


