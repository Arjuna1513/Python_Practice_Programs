import sys

try:
    f = open('mytext.txt')
    s= f.readline()
    i = int(s.strip())
except OSError as err:
    print(err)
except ValueError:
    print("Could not convert data to an integer.")
except:
     print("Unexpected Error:", sys.exc_info()[2])
     # raise
    # pass

"""
sys.exc_info()

the values returned are (type, value, traceback). Their meaning is: type gets the exception 
type of the exception being handled (a class object); value gets the exception parameter 
(its associated value or the second argument to raise, which is always a class instance 
if the exception type is a class object); traceback gets a traceback object 
(see the Reference Manual) which encapsulates the call stack at the point where the 
exception originally occurred.

sys.exc_info()[0] returns exception class
sys.exc_info()[1] returns exception value
sys.exc_info()[2] returns stacktrace value
sys.exc_info()[3] returns tuple index out of range error
"""