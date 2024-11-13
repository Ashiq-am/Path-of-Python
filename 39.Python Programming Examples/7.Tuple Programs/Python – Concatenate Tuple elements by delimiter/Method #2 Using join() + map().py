# Python3 code to demonstrate working of
# Concatenate Tuple elements by delimiter
# Using join() + map()

# initializing tuple
test_tup = ("Gfg", "is", 4, "Best")

# printing original tuple
print("The original tuple is : " + str(test_tup))

# initializing delim
delim = "-"

# for joining, delim is used
res = delim.join(map(str, test_tup))

# printing result
print("Concatenated Tuple : " + str(res))
