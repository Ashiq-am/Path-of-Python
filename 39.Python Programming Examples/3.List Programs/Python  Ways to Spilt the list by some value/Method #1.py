# Python code to split the list
# by some value into two lists.

# List initialisation
list = ['Geeks', 'forgeeks', 'is a', 'portal', 'for Geeks']

# Splitting list into first half
first_list = list[:list.index('forgeeks')]

# Splitting list into second half
second_list = list[list.index('forgeeks')+1:]

# Printing first list
print(first_list)

# Printing second list
print(second_list)
