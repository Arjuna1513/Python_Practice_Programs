from Multiple_Inheritence.first import First

class Second(First):
    def __init__(self):
        print("Second class Constructor")
        super().__init__()

    def firstMethod(self):
        print("Base second class FirstMethod")

    def secondMethod(self):
        print("Base second Class secondMethod")