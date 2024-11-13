# Python3 code to demonstrate working of
# Incremental Size Chunks from Strings
# Using generator + slicing

# generator function
def gen_fnc(test_str):
    strt = 0
    stp = 1
    while test_str[strt: strt + stp]:
        # return chunks runtime while looping
        yield test_str[strt: strt + stp]
        strt += stp
        stp += 1


# initializing string
test_str = 'geekforgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# calling fnc.
res = list(gen_fnc(test_str))

# printing result
print("The Incremental sized Chunks : " + str(res))
