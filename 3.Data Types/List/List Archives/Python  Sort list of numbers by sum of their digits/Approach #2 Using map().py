# Python3 Program to Sort list of
# integers according to sum of digits

def sortList(num):
    return sum(map(int, str(num)))


# Driver Code
lst = [12, 10, 106, 31, 15]
result = sorted(lst, key=sortList)
print(result)
