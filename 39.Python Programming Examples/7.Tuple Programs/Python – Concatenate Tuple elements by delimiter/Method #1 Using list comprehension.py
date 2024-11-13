# Python3 code to demonstrate working of
# Concatenate Tuple elements by delimiter
# Using list comprehension

# initializing tuple
test_tup = ("Gfg", "is", 4, "Best")

# printing original tuple
print("The original tuple is : " + str(test_tup))

# initializing delim
delim = "-"

# using str() to convert elements to string
# join to convert to string
res = ''.join([str(ele) + delim for ele in test_tup])

# striping stray char
res = res[ : len(res) - len(delim)]

# printing result
print("Concatenated Tuple : " + str(res))
