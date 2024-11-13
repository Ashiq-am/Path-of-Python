# Python3 program to Sort list
# containing alpha and numeric values

def sort(lst):
    return sorted(lst, key=str)


# Driver code
lst = ['k', 5, 'e', 3, 'g', 7, 0, 't']
print(sort(lst))
