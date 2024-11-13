# Python program to demonstrate
# defaultdict


from collections import defaultdict

# Defining the dict
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

# Provides the default value
# for the key
print(d.__missing__('a'))
print(d.__missing__('d'))
