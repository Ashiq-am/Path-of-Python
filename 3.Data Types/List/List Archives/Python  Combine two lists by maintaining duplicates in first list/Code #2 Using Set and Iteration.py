# Python code to combine two lists
# and removing duplicates, without
# removing duplicates in original list.

# Initialisation of first list
list1 = [11, 22, 22, 15]

# Initialisation of Second list
list2 = [22, 15, 77, 9]

# creating set
unique_list1 = set(list1)
unique_list2 = set(list2)

# Difference in two sets
diff_element = unique_list2 - unique_list1

# union of difference + first list
output = list1 + list(diff_element)

# printing output
print(output)
