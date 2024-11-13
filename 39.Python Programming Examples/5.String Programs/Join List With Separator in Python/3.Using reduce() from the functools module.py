from functools import reduce

# List Data
my_list = ["GFG", "Java", "DSA"]

# Taking ',' as a separator
separator = ", "

# Applying Lambda function in reduce method
joined_string3 = reduce(lambda x, y: x + separator + y, my_list)

print("Before Joining: ", my_list)
print("After Joining: ", joined_string3)
