# factorial function
def factorial(i):

    if i<0:
        return None

    if i == 0:
        return 1


    return i * factorial(i-1)

# passing an integer to the function
print(factorial(4))

# passing a string to the function
print(factorial("4"))

# passing a floating point number to the function
print(factorial(5.01))
