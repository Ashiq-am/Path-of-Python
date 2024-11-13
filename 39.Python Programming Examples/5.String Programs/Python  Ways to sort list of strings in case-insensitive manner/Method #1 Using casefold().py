# Python code to demonstrate
# to sort list of
# strings in case insensitive manner

# Initialsing list
ini_list = ['akshat', 'garg', 'GeeksForGeeks', 'Alind',
            'SIngh', 'manjeet', 'Munich']

# Sorting list in case sensitive manner
res1 = sorted(ini_list)

# Printing case-insensitive
print("Case-sensitive sorted list", str(res1))

# Sorting list in case-insensitive manner
res2 = sorted(ini_list, key=lambda s: s.casefold())

# Printing result
print("Case-insensitive sorted list", str(res2))

