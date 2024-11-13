# Python code to demonstrate that a function
# can easily return multiple values.
def multi_return(*arr):
    k1 = arr[0]
    k2 = arr[1]
    return k1, k2


a, b = multi_return(11, 22)
print(a, ' ', b)

a, b = multi_return(55, 66, 77, 88, 99)
print(a, ' ', b)
