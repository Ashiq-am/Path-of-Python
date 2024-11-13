# Creating a dictionary
myDict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Iterating through the keys
for key in myDict.keys():
	if key == 2:
		del myDict[key]

# Modified Dictionary
print(myDict)
