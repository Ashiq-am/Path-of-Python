# List Data
my_list = ["GFG", "Java", "DSA"]

# Taking ',' as a separator
separator = ", "

# Converting list elements to string using map then joining them
joined_string2 = separator.join(map(str, my_list))

print("Before Joining: ", my_list)
print("After Joining: ", joined_string2)
