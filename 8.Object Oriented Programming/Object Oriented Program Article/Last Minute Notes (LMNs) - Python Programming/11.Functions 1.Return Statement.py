# function with no parameters and no return statement
def fun():
    print("fun() called!")


# function with parameters but no return statement
def printSum(a, b):
    print("sum = ", a + b)


# function with no parameters with return statement
def greet():
    return "Hello!"


# function with parameters and return statement
def getSum(a, b):
    return a + b


fun()
printSum(3, 5)
print(greet())
print(getSum(3, 5))
