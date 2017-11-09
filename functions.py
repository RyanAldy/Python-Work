# Nested function example - calling functions in functions

def myFunction(x):
    if x == 1:
        def myprint():
            for a in range(11):
                print(a)
    elif x == 2:
        def myprint():
            print("Hello my friends!")
    else:
        def myprint():
            print("***")
    # Return function
    return myprint

#Store returned value / function from function into F
F = myFunction(1)
# Call function
F()
A = myFunction(2)
A()
B = myFunction(100)
B()
