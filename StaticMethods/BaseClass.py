class BaseClass:

    @staticmethod
    def staticMethod():
        print("I am a static method in base class")

    def instanceMethod(self):
        print("I am an instance method")

    @classmethod
    def classMethod(cls):
        print("I am a class method in base class")