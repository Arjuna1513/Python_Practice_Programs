class MyClass:
    def method1(self):
        print("Method 1")
        self.method2()

    def method2(self):
        print("Method 2")

    def method3(self):
        print("Method 3")

    def method4(self):
        print("Method 4")

x = MyClass()
x.method1()