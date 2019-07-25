class Car():

    def __init__(self, brand):
        self.brand = brand

    def turboEngine(self):
        print("Turbo Engine")

class Maruthi(Car):
    def __init__(self, model):
        self.model = model
        super(Maruthi, self).__init__("Car")

    def gears(self):
        print("6 gears")

c1 = Car("Maruthi")
print(c1.brand)
c1.turboEngine()