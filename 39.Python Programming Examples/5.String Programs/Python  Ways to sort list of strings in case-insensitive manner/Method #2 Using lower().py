# Python code to demonstrate
# to sort list of
# strings in case insensitive manner

# Initialsing list
ini_list = ['akshat', 'garg', 'GeeksForGeeks', 'Alind',
            'SIngh', 'manjeet', 'Munich']

# Sorting list in case sensitive manner
ini_list.sort()

# Printing case-insensitive
print("Case-sensitive sorted list", str(ini_list))

# Sorting list in case-insensitive manner
ini_list.sort(key=lambda x: x.lower())

# Printing result
print("Case-insensitive sorted list", str(ini_list))

