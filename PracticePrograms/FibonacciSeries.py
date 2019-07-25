a = 0
b = 1
fib = [a, b]
result = 0

tillWhere = int(input("Enter the value"))

for i in range(2, tillWhere+1):
    result = fib[i-2]+fib[i-1]
    fib.append(result)

for value in fib:
    print(value)
