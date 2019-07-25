val1 = 100
val2 = 200
try:
    val3 = val1 + val2
    raise FileNotFoundError

except Exception:
    print("I am an Exception")
except BaseException:
    print("I am Base Exception")
except FileNotFoundError:
    print("FileNotFound Exception")

"""
Observe this here : I have thrown raise FileNotFoundError exception and I have even defined
except block with FileNotFoundError exception but here the exception is caught by first one
i.e. Exception itself because in the exceptions hierarchy BaseException-->Exception-->FileNotFoundError
so when the exception is thrown the first one to catch is Exception and it holds true because 
FileNotFoundError exception is child class of Exception but however in java when the above hierarchy is 
given compiler says error with message "Unreachable Code"
"""