# Python3 code to demonstrate working of
# Convert String to list of tuples
# Using zip() + list slicing + split()

# initialize string
test_string = "GFG is best Computer Science Portal"

# printing original string
print("The original string : " + str(test_string))

# Convert String to list of tuples
# Using zip() + list slicing + split()
temp = test_string.split()
res = list(zip(temp[::2], temp[1::2]))

# printing result
print("List after String to tuple conversion : " + str(res))
