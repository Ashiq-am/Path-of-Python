# Python3 program to Merge first and last
# elements separately in a list of lists

def merge(lst):
    return [list(ele) for ele in list(zip(*lst))]


# Driver code
lst = [['x', 'y'], ['a', 'b'], ['m', 'n']]
print(merge(lst))
