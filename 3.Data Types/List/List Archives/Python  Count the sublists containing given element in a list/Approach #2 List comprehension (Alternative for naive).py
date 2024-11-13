# Python3 Program to count number of
# list containing a certain element
# in a list of lists

def countList(lst, x):
    return sum(x in item for item in lst)


# Driver Code
lst = (['a'], ['a', 'c', 'b'], ['d'])
x = 'a'
print(countList(lst, x))
