# Python code to find key with Maximum value in Dictionary

# Dictionary Initialization
Company = {'GFG':10000, 'Hashd':2292, 'Infy': 200}

# taking list of car values in v
v = list(Company.values())

# taking list of car keys in v
k = list(Company.keys())

print(k[v.index(max(v))])
