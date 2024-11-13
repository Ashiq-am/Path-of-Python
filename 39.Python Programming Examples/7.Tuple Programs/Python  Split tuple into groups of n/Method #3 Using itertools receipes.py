# Python code to demonstrate
# how to split tuple
# into the group of k-tuples

# function to group tuple into groups of 4
def grouper(n, iterable):
    args = [iter(iterable)] * n
    return zip(*args)


# initialising tuple
ini_tuple = (1, 2, 3, 4, 8, 12, 3, 34,
             67, 45, 1, 1, 43, 65, 9, 10)

# printing initial tuple
print("initial list", str(ini_tuple))

# code to group
# tuple into size 4 tuples
res = tuple(grouper(4, ini_tuple))

# printing result
print("resultant tuples", str(res))
