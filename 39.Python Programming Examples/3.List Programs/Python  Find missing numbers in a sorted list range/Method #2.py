# Python3 program to Find missing
# integers in list

def find_missing(lst):
    return [i for x, y in zip(lst, lst[1:])
            for i in range(x + 1, y) if y - x > 1]


# Driver code
lst = [1, 2, 4, 6, 7, 9, 10]
print(find_missing(lst))
