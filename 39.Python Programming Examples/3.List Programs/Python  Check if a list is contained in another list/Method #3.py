# Python3 program to Remove elements of
# list that repeated less than k times


def removeElements(A, B):
    return ', '.join(map(str, A)) in ', '.join(map(str, B))


# Driver code
A = ['x', 'y', 'z']
B = ['x', 'a', 'y', 'x', 'b', 'z']
print(removeElements(A, B))
