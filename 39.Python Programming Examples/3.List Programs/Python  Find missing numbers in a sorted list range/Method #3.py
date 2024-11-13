# Python3 program to Find missing
# integers in list

def find_missing(lst):
    return sorted(set(range(lst[0], lst[-1])) - set(lst))


# Driver code
lst = [1, 2, 4, 6, 7, 9, 10]
print(find_missing(lst))
