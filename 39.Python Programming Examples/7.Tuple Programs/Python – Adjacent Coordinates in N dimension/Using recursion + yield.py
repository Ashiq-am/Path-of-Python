# Python3 code to demonstrate working of
# Adjacent Coordinates in N dimension
# Using recursion + yield

# helper_fnc
def adjac(ele, sub = []):

    if not ele:
        yield sub

    else:
        yield from [idx for j in range(ele[0] - 1, ele[0] + 2)
                    for idx in adjac(ele[1:], sub + [j])]

# initializing tuple
test_tup = (3, 4)

# printing original tuple
print("The original tuple : " + str(test_tup))

# Initialize dictionary keys with Matrix
# Using deepcopy()
res = list(adjac(test_tup))

# printing result
print("The adjacent Coordinates : " + str(res))
