var = 100

def method():
    global var
    print(f"Value of variable var is {var}")
    var = 200
    print(f"Value of variable var after changing is {var}")

method()
print(f"Value of global variable var is {var}")

# Here in the method we have mentioned the var variable to be global variable var defined outside method
# so the method uses global var not the local var. 