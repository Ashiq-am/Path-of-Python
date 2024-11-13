# Python3 code heck multiple key existence
# using issubset

# initializing a dictionary
sports = {"geeksforgeeks" : 1, "practice" : 2, "contribute" :3}

# creating set of keys that we want to compare
s1 = set(['geeksforgeeks', 'practice'])
s2 = set(['geeksforgeeks', 'ide'])

print(s1.issubset(sports.keys()))
print(s2.issubset(sports.keys()))
