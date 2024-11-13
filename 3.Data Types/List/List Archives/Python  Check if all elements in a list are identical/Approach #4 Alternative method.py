# Python3 program to check if
# all elements in a list are identical
def check(x):
    return x and [x[0]] * len(x) == x


# Driver code
print(check(['a', 'b', 'c']))
print(check([1, 1, 1]))
