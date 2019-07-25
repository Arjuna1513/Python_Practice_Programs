listValues = ['Nakula', 'Sahadeva', 'Bhima', 'Arjuna', 'dritharastra']

size = listValues.__len__()

# __len__() method returns the size of list.
print(f"size of list is : {size}")

print(listValues[0])
print(listValues[1])
print(listValues[2])
print(listValues[3])
print(listValues[4])

#print(listValues[5]) list index out of range error

print(listValues[size-1])
#the above accessess the last element present in a list