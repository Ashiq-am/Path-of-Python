# Python3 Program to Create list
# with integers within given range

def createList(r1, r2):
    return [item for item in range(r1, r2 + 1)]


# Driver Code
r1, r2 = -1, 1
print(createList(r1, r2))
