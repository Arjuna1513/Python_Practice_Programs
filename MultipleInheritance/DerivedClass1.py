from MultipleInheritance.BaseClass import BaseClass

class DerivedClass1(BaseClass):
    def __init__(self, bca, bcb, dc1, dc2):
        self.dc1 = dc1
        self.dc2 = dc2
        super(DerivedClass1, self).__init__(bca, bcb)

    def dc1Method(self):
        print("Derived class cdMethod")


dc1 = DerivedClass1(1, 2, 3, 4)
dc1.bcMethod1()
dc1.bcMethod2()
dc1.dc1Method()
print(dc1.dc1)
print(dc1.dc2)
print(dc1.bca)
print(dc1.bcb)
