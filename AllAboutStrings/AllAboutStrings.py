String1 = "Mallikarjuna"
String2 = 'Mallikarjua'
String3 = """Mallikarjuna B"""

#print(String1, String2, String3, sep=',\t')

#String4 = String1 + String2
#print(String4)

"""
del String1
print(String1) # throws error because u have already deleted a String1
"""

"""
String1[0] = 9
print(String1) # throws error because strings are immutable:
"""

"""
del String1[0]
print(String1) # throws error because string does not support deletion by index.
"""

"""string4 = 'Bhishma'
print(string4[0])
# print(string4[len(string4)]) # index out of range
print(string4[len(string4)-1])

for x in string4:
    print(x, end='\t')
print('\n')

# Reverse a String
print(string4[::-1])
"""

string5 = 'Bhishma5'
"""
print(string5[2:5]) # prints chars starting from 2 to 4

print(string5[0:len(string5)]) # prints starting from zero till the length of the string i.. prints entire string.

print(string5[1:len(string5):2])

print(string5[-2]) # prints the value present at the given index beginning from end of file.

print(string5[1:]) # prints everything that begins from index 1.

print(string5[:5]) # prints everything that comes till index 5(excluding)
"""

"""
print(string5[-3:]) # prints everything that comes till index 3(inclusive)

print(string5[:-3]) # prints everything that comes after 3rd index(exclusive)

print(string5[-5:-3]) # prints between index -3(inclusive) and -5(exclusive)
"""

print(string5.count('h')) # prints total occurances of letter 'h' in string.

print(string5.count('h', 2, len(string5)-1))
# returns the total number of occurences of letter 'h' starting from 2nd index and till the end index mentioned.

print(string5.index('h'))

print(string5.index('h', 2, 7)) #displays the index of 'h' character starting from 2nd index.

string6 = '  Hello  '
print(string6.strip()) # it won't really removed the spaces from string6, it just created one more string
# with no spaces.
print(string6)

print(string5.capitalize())
print(string5.casefold())
print(string5.find('hi')) # displays the start index of the str mentioned
print(string5.find('sh', 3, 6)) # displays the index of the pattern mentioned starting from 3 rd index
# and till the index 6.
print(string5.endswith('a')) # returns true if string ends with letter a else returns false.
print(string5.endswith('h', 0, 5)) # returns true if string end with letter 'h' at index 4 beginning from 0 else
# returns false...
print(string5.isalnum()) # displays true if string is alpha numeric.
print(string5.isalpha()) # displays true if string is only alpha else displays false.
print(string5.isdigit()) # displays true if string is of digits else displays false.
print(string5.islower()) # displays true if all the characters in string are lower characters.
print(string5.isupper()) # displays true if all the characters in the string are upper case letters.
print(string5.isspace()) # displays true if the string is a space else false.
print(string5.join('abc')) # outputs aBhishma5bBhishma5c
print(string5.lower()) # displays all the characters in lower letters.
print(string5.find('h')) # displays the index of first occurence of letter 'h'
print(string5.rfind('h')) # displays the index of last occurence of letter 'h'
print(type(string5.split('h'))) # splits the string based in the provided input o/p is ['B', 'is', 'ma5'] and
# returns the list just like java returns an array.
string6 = 'I am an human'
print(string6.partition('am'))
# o/p is ('I ', 'am', ' an human') i.e. it returns a tuple and everything as a string that comes
# before separator and separator as a string and everything that comes after separator as a string
# and if sep is not found then the entire string followed by 2 empty strings.

print(string5.__getitem__(5)) # returns the char present at given index value


