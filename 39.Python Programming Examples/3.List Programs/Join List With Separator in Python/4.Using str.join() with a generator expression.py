# List Data
my_list = ["GFG", "Java", "DSA"]

# Taking ',' as a separator
separator = ", "

# Using generator function to iterate every element and then joining them
joined_string4 = separator.join(item for item in my_list)

print("Before Joining: ", my_list)
print("After Joining: ", joined_string4)
