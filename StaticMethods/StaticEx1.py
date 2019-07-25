# @staticmethod
# def printData():
#     print("Hello India")
#
# print(printData())

# static methods cannot be used as normal functions. i.e. static methods should be defined.
# in classes only

class StaticEx1:

    classVar = 100
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def intanceMethod1(self):
        print(f"values of variables are: {self.x} {self.y}")

    @classmethod
    def classMethod(cls):
        # print(f"values are as follows : {cls.x}  {cls.y}")
        # since x and y are instance variables we cannot access them using cls.
        # print("Let's change the values of obj variables:")
        # cls.x = 111
        # cls.y = 222
        # print(f"values after changing are as follows : {cls.x}  {cls.y}")
        print(f"I can access class variables : {cls.classVar}")
        # since the classVar is at class level we can access them using @classmethod methods
        obj = StaticEx1(99, 88)
        print(f"class method can create an object and then can access variables : {obj.x}  {obj.y}")
        cls.classVar = 999

    """
    Just like in java we cannot access instance variables in static method directly but however we can
    create the instance of the object in the static method and can access the values which again
    doesn't make sense since the purpose of static method is different...
    """
    @staticmethod
    def staticMethod():
        print("I cannot access instance variables")
        obj2 = StaticEx1(33, 44)
        print(f"values are {obj2.x}  {obj2.y}")
        # I cannot access classVar as well, becoz i dont have cls parameter.


obj = StaticEx1(100, 200)
obj.intanceMethod1()  # used object to call instance method

obj.staticMethod() # even though we are able to call static method with object bt internally what
# python does is it will not send the self of the object to static method when called using object
# hence u ll not be able to access instance variables using static methods in python.

obj.classMethod()
print(obj.classVar)



