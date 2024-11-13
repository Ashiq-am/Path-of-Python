# Python3 Program to count number of
# list containing a certain element
# in a list of lists

def countList(lst, x):
    count = 0
    for i in range(len(lst)):
        if x in lst[i]:
            count += 1

    return count


# Driver Code
lst = (['a'], ['a', 'c', 'b'], ['d'])
x = 'a'
print(countList(lst, x))
