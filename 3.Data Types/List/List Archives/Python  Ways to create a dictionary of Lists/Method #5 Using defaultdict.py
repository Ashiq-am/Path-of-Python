# Importing defaultdict
from collections import defaultdict

lst = [('Geeks', 1), ('For', 2), ('Geeks', 3)]
orDict = defaultdict(list)

# iterating over list of tuples
for key, val in lst:
	orDict[key].append(val)

print(orDict)
