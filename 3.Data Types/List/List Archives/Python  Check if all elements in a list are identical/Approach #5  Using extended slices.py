# Python3 program to check if
# all elements in a list are identical
def check(list):
    return list[1:] == list[:-1]


# Driver code
print(check(['a', 'b', 'c']))
print(check([1, 1, 1]))
