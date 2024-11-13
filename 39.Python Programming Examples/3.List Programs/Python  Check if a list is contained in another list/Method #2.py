# Python3 program to Remove elements of
# list that repeated less than k times

def removeElements(A, B):
    n = len(A)
    return any(A == B[i:i + n] for i in range(len(B) - n + 1))


# Driver code
A = [1, 2]
B = [1, 2, 3, 1, 1, 2, 2]
print(removeElements(A, B))
