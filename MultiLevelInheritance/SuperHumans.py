from MultiLevelInheritance.Humans import  Humans

class SuperHumans(Humans):
    def __init__(self, lifespan, color, legs, hands, IQ):
        self.IQ = IQ
        super(SuperHumans,self).__init__(legs, hands, lifespan, color)

    def walks(self):
        print("Walks Smartly")

sh = SuperHumans(33, 'varies', 2, 2, 'High')
sh.walks()
sh.sleep()
sh.eats()

"""
Here Mammals is a base class
Humans extends Mammals
SuperHumans extends Humans
Constructor chaining is in place here.
"""
