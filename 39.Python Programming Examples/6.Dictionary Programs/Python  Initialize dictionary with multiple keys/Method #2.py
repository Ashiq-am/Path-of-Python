# Python3 code to demonstrate working of
# Initialize dictionary with multiple keys
# Using fromkeys()

# Initialize keys
test_keys = ['gfg', 'is', 'best']

# Using fromkeys()
# Initialize dictionary with multiple keys
res ={ **dict.fromkeys(test_keys, 4)}

# printing result
print("Dictionary after Initializing multiple key-value : " + str(res))
