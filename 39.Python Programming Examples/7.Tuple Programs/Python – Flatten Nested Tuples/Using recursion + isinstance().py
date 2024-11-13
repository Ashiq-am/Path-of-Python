# Python3 code to demonstrate working of
# Flatten Nested Tuples
# Using recursion + isinstance()

# helper function
def flatten(test_tuple):
    if isinstance(test_tuple, tuple) and len(test_tuple) == 2 and not isinstance(test_tuple[0], tuple):
        res = [test_tuple]
        return tuple(res)

    res = []
    for sub in test_tuple:
        res += flatten(sub)
    return tuple(res)


# initializing tuple
test_tuple = ((4, 5), ((4, 7), (8, 9), (10, 11)), (((9, 10), (3, 4))))

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Flatten Nested Tuples
# Using recursion + isinstance()
res = flatten(test_tuple)

# printing result
print("The flattened tuple : " + str(res))
