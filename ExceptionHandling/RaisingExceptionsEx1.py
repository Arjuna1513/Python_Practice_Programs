
val1 = 100
val2 = 200

try:
    raise ZeroDivisionError("I raised this exception")
except ZeroDivisionError as err:
    print(err)

# when u raise an Exception u can even send the argument to the constructor of the Exception and when the
# Exception message is displayed in console.