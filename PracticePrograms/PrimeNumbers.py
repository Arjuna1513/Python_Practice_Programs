#program to find prime numbers...

value = int(input("Enter the value"))

for i in range(2,value):
    if value % i == 0:
        print(f"Entered number {value} is not a prime number")
        exit(0)

print(f"Entered number {value} is a prime number")
