# Python3 code to demonstrate
# Filter String with substring at specific position
# using list comprehension + list slicing

# Initializing list
test_list = ['geeksforgeeks', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list is : " + str(test_list))

# Initializing substring
sub_str = 'geeks'

# Initializing range
i, j = 0, 5

# Filter String with substring at specific position
# using list comprehension + list slicing
res = [ele for ele in test_list if ele[i: j] == sub_str]

# printing result
print ("Filtered list : " + str(res))
