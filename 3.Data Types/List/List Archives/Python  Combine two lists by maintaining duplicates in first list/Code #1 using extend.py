# Python code to combine two lists
# and removing duplicates, without
# removing duplicates in original list.

# Initialisation of first list
list1 = [111, 222, 222, 115]

# Initialisation of Second list
list2 = [222, 115, 77, 19]

output = list(list1)

# Using extend function
output.extend(y for y in list2 if y not in output)

# printing result
print(output)
