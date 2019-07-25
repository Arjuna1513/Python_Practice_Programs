class MethodOverLoading:
    def add(self, a, b=0, c=0, d=0):
        return a+b+c+d

x = MethodOverLoading()
print(x.add(10,20,30,40))
print(x.add(10))
print(x.add(11,22))
print(x.add(11,22,33))