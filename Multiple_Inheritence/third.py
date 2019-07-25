from Multiple_Inheritence.first import First
from Multiple_Inheritence.second import Second

class Third(First,Second):
    def __init__(self):
        super().__init__()
        print("Third class Constructor")

    def ThirdClassMethod(self):
        print("Derived class's Method")

    # def __str__(self):
    #     print("Overridden __str__ method")

    # def firstMethod(self):
    #     print("Derived class's Third class Method")
    #
    # def secondMethod(self):
    #     print("Derice class's Third class Method")

x = Third()
x.firstMethod()
x.secondMethod()



"""
In the above, Third class extends both first and second classes and in the first and second class we have
firstMethod() and secondMethod() and we have constructors in both class First and Class Second.

Now when we override those methods firstMethod and secondMethod in Third class and when we call
x = Third()
x.firstMethod()
x.secondMethod()

Then since we have 
class Third(First,Second):
    def __init__(self):
        super().__init__()
        print("Third class Constructor")
Then First class constructor will be called because we have First,Second in order from left to Right.
similarly firstMethod and secondMethod will be searched in THirdClass and if present it will be called 
If not overridden in the Third class then it will be searched in First class first because that
comes first in the Third class extended list of classes.

so the output will be 
First class Constructor
Third class Constructor
Base First class FirstMethod
Base First class SecondMethod

This is called Python MRO(Method Resolution Order)
which states that the order of method resolution is DepthFirst and then from left to right.

"""