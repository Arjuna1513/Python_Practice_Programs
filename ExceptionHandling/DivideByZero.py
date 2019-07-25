val1 = int(input("Enter integer variable1 here-->>>"))
val2 = int(input("Enter integer variable2 here-->>>"))

try :
    var3 = val1/val2
    print(f"Result of var1/var2 is : {var3}")
except ZeroDivisionError:
    print(f"Value of var2 must be greater than zero")
finally:
    print("I will always be executed")

# The above one throws ZeroDivisionError if the val2 is 0 so put the above line in try block


