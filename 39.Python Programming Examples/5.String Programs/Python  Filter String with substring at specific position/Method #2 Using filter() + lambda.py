# Python3 code to demonstrate
# Filter String with substring at specific position
# using filter() + lambda

# Initializing list
test_list = ['geeksforgeeks', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list is : " + str(test_list))

# Initializing substring
sub_str = 'geeks'

# Initializing range
i, j = 0, 5

# Filter String with substring at specific position
# using filter() + lambda
res = list(filter(lambda ele: ele[i: j] == sub_str, test_list))

# printing result
print ("Filtered list : " + str(res))
