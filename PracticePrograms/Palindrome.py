num = int(input("Enter a number here->>"))
result = int(0)
value = num
print(result)

while num != 0:
    digit = num % 10
    result = result * 10 + digit
    print(result)
    num = num // 10

#in python to divide please use // instead of / 

#print(num)
print(result)

if value == result:
    print("Palindrome")

else:
    print("Not a palindrome")