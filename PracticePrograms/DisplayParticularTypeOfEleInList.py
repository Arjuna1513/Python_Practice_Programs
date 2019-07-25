listValues = [1, 'Arjun', 22.22, 100, "Bhishma"]

for element in listValues:
    if type(element) == str or type(element) == float:
        print(element)

str1 = "Arjuna"
str2 = "Arjunaa"

if str1.__eq__(str2):
    print("Both are equal")