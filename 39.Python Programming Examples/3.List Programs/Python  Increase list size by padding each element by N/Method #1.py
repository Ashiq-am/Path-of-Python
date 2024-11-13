# Python3 program to increase list size
# by padding each element by N

def increaseSize(lst, N):
    return [el for el in lst for _ in range(N)]


# Driver code
lst = [1, 2, 3]
N = 3
print(increaseSize(lst, N))
