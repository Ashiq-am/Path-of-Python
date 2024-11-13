# Python3 program to check if
# all elements in a list are identical
def check(list):
    return all(i == list[0] for i in list)


# Driver code
print(check(['a', 'b', 'c']))
print(check([1, 1, 1]))
