class SampleClass:
    pass

    def __str__(self):
        return "The address of string is 00000XXXXX00000"

sc = SampleClass()
print(sc)

#  Here __str__() is equal to toString() method in java and we have overridden that method to give our
# implementation for that method, every class extends object class and SampleClass does too.