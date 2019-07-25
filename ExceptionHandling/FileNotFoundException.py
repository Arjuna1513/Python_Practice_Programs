# f = None
# text = None
text = None
try:
    with open("file1.txt", 'r') as f:
        text = f.read()
except FileNotFoundError:
    print("File doesn't exist")
finally:
    print("No need to explicitly close the file since python takes care of it when we use with open() as f")

# The above line throws FileNotFoundError so put the above code in try block
print(text)

# Exception throws when file is not present since the file is open in read mode.