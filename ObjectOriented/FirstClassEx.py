class Dog():

    def __init__(self, breed, color, name, barks):
        self.breed = breed
        self.name = name
        self.color = color
        self.barks = barks

# myDog = Dog(breed = 'Raja Palyam')
myDog = Dog('Raja Palyam', 'Milky White', 'Raja', True)

print(f"The details of dog object are as follows --> \n breed :{myDog.breed} \n name :{myDog.name}\n"
      f" color:{myDog.color} \n and barks: {myDog.barks}")

# self is just like 'this' operator we use in java programming...
#  you can use other word instead of self but self is used usually bcoz it's self explaining

#  Let's add more attributes color, name and spots