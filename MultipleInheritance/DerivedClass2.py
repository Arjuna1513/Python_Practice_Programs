from MultipleInheritance.BaseClass import BaseClass

class DerivedClass2(BaseClass):
    def __init__(self, bca, bcb, dc2a, dc2b):
        self.dc2a = dc2a
        self.dc2b = dc2b
        super(DerivedClass2, self).__init__(bca, bcb)

    def dc1Method(self):
        print("Derived class cdMethod")


dc = DerivedClass2(1, 2, 3, 4)
dc.bcMethod1()
dc.bcMethod2()
print(dc.dc2a)
print(dc.dc2b)
print(dc.bca)
print(dc.bcb)


"""
Here DerivedClass1 and DerivedClass2 both have extended the baseclass.
"""