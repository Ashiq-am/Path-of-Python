# Python3 Program to Sort list of
# integers according to sum of digits

def sortList(lst):
    digits = [int(digit) for digit in str(lst)]
    return sum(digits)


# Driver Code
lst = [12, 10, 106, 31, 15]
print(sorted(lst, key=sortList))
