from InheritanceEx.Animal1 import Animal1

class Dog1(Animal1):
    def __init__(self, lifespan):
        self.lifespan = lifespan
        super(Dog1, self).__init__()
        pass

    def makesNoise(self):
        print("Woof!")

d1 = Dog1(12)
d1.makesNoise()
d1.eat()




