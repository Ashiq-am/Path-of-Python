# Python3 code to demonstrate working of
# Convert String to list of tuples
# Using iter() + split() + next() + generator expression

# initialize string
test_string = "GFG is best Computer Science Portal"

# printing original string
print("The original string : " + str(test_string))

# Convert String to list of tuples
# Using iter() + split() + next() + generator expression
temp = iter(test_string.split())
res = [(ele, next(temp)) for ele in temp]

# printing result
print("List after String to tuple conversion : " + str(res))
