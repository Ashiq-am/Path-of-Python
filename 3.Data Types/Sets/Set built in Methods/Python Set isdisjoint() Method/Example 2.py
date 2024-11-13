# Set
A = {2, 4, 5, 6}

# List
lis = [1, 2, 3, 4, 5]

# Dictionary dict, Set is formed on Keys
dict = {1: 'Apple', 2: 'Orage'}

# Dictionary dict2
dict2 = {'Apple': 1, 'Orage': 2}

print("Set A and List lis disjoint?", A.isdisjoint(lis))
print("Set A and dict are disjoint?", A.isdisjoint(dict))
print("Set A and dict2 are disjoint?", A.isdisjoint(dict2))
