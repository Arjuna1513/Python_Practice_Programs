class Access_Modifiers:
    def __init__(self, a):
        self.__var = a

    def method1(self):
        print("Instance Public Method")

    def __method2(self):
        print("Instance private method")

if __name__ == "__main__":
    x = Access_Modifiers(100)
    print(x._Access_Modifiers__var)
    print(x._Access_Modifiers__method2())


"""
In the above, variables/members defined with __ will be treated as private. It is not a rule but
convention followed in python. When we define a method/variable with __, python does mangling of the 
variables which means it will append _ClassName with it so to access the __ variables in a class
one should use objectname._Classname__variableName as shown above:
    print(x._Access_Modifiers__var)
    print(x._Access_Modifiers__method2())
    
U may get a doubt but still we are able to access, but as I already mentioned it is not a rule
which means it will not prevent u from accessing it but this may at least will prevent from
accidental overriding of the method in case of inheritance.


_ when used with variable/method name it means that it is a protected variable which again
means this should be used by the same class or the class that inherits it.

But again it is just a convention, it can be access by another class which is not a subclass of the
class of the _ variable.
"""