elements = [5, 4, 15, 20, 25]
size = 0

for ele in elements:
    size = size + 1
#print(size)

for i in range(0, size):
    for j in range(0, size-1):
        if elements[j+1] > elements[j]:
            temp = elements[j]
            elements[j] = elements[j+1]
            elements[j+1] = temp

for number in elements:
    print(number)
