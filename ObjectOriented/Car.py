class Car():
    rpm = 10000
    def __init__(self, model1, price1, mileage1, brand1):
        self.model = model1
        self.price=price1
        self.mileage = mileage1
        self.brand=brand1

    def display(self):
        print(f"Price of {self.model} car is {self.price}")


c1 = Car('ertiga', 100000, '22kmph', 'maruthi')
c1.display()
print(c1.rpm)
c2 = Car('swift', 100000, '21kmph', 'maruthi')
print(c2.rpm)
Car.rpm = 88888
c1.rpm=111111
print(c1.rpm)
print(c2.rpm)
c2.rpm=99
print(c2.rpm)
Car.rpm = 77777

print(c1.rpm)
print(c2.rpm)

# When we observe, rpm was declared as 10000,
# so when we initialize variable outside init all the objects will have the same value.
# now if i change that value for any object then the value of that variable of object
# will get changed.
# now if i change class variable using Car.rpm = 666666 and now if u view this value of objects
# except for the object which has changed its value of this variable, all other objects will have the
# latest value.
# But make sure that we have given it as a class variable thinking that it's value remains same through
# out, but if u need something which varies from object to object then declare that a instance variable.
# and we know that we can access class variable using objects but always use using class name.
# self is like "this" operator we use in java.