# Creating a dictionary
myDict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Iterating through the list of keys
for key in list(myDict):
	if key == 2:
		del myDict[key]

# Modified Dictionary
print(myDict)
