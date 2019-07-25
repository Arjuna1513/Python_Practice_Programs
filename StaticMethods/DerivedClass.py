from StaticMethods.BaseClass import BaseClass

class DerivedClass(BaseClass):

    def derivedClassMethod(self):
        print("I am a method from derived class")

    @staticmethod
    def staticMethod():
        print("I am an overridden static method from Derived class")

    @classmethod
    def classMethod(cls):
        print("I am a class method in derived class")

c1 = DerivedClass()
c1.derivedClassMethod()
c1.instanceMethod()
DerivedClass.staticMethod()
DerivedClass.classMethod()


# we can override instance/static as well as 