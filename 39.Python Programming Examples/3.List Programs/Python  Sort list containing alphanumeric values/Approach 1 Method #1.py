# Python3 program to Sort list
# containing alpha and numeric values

def sort(lst):
    lst = [str(i) for i in lst]
    lst.sort()
    lst = [int(i) if i.isdigit() else i for i in lst]
    return lst


# Driver code
lst = ['k', 5, 'e', 3, 'g', 7, 0, 't']
print(sort(lst))
