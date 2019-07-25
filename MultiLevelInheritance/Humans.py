from MultiLevelInheritance.Mammals import  Mammals

class Humans(Mammals):
    def __init__(self, legs, hands, lifespan, color):
        self.legs = legs
        self.hands = hands
        Mammals.__init__(self, lifespan, color)
        #super(Humans, self).__init__(lifespan, color) above 1 and this one both works fine.

    def walks(self):
        print("Walks using legs")

    def sleep(self):
        print("Usually sleeps for 7 hours")

# h1 = Humans(2, 2, 35, 'varies')
# print(f"Variables values are : {h1.lifespan}, {h1.color}, {h1.hands}, {h1.legs}")
# h1.eats()
# h1.sleep()
# h1.walks()

"""
If we have parameters defined in constructor and if we do not pass values in constructor then we get
TypeError: __init__() missing 4 required positional arguments: 'legs', 'hands', 'lifespan', and 'color'
so to avoid that just pass parameters while creating an object.

Here i have overridden sleeps and walks methods hence overridden methods of Humans class gets called.
since we have not overridden eats method, eats method of Mammals class gets called.
"""

# m1 = Mammals(33, 'Varies')
# print(m1.color)
# print(m1.lifespan)
# print(m1.legs) # this will throw error because legs is an attribute of child class.
# Parent reference to child object: