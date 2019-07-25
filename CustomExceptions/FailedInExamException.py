class FailedInExamException(Exception):
    def __init__(self, marks):
        # self.errMessage = errMessage
        self.marks = marks

    def verification(self):
        try:
            if self.marks < 35:
                raise FailedInExamException(f"U have scored marks less than: {self.marks}")
            else:
                print("U r passed in exam")
        except FailedInExamException as err:
            print(err.marks)

marks = None
while True:
    try:
        marks = int(input("Enter Marks here-->"))
        break
    except:
        print("Please enter integer marks less than or equal to 100")
x = FailedInExamException(marks)
x.verification()


"""
Here FailedInExamException is a custom exception that extends Exception class and I have defined a 
method verification which evaluates the marks of the self object with 35 and if self object marks is
less than 35 then a custom exception FailedInExamException is throws, remember here that this exception
is again a new object of type FailedInExamException() with a parameter 
f"U have scored marks less than: {self.marks}" i.e. this new object's marks value will be the parameter
that we have passed so this new object will have a marks value as f"U have scored marks less than: {self.marks}"
unlike in java where the type of instance variable is predefined here the type of value depends on the
value we pass. same variable of Two objects of same class can contain value of different data type
below is the proof
"""

x1 = FailedInExamException(11)
x2 = FailedInExamException("Hello babe")
print(x1.marks)
print(x2.marks)