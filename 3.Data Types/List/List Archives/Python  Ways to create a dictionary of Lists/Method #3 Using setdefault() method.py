# Creating an empty dict
myDict = dict()

# Creating a list
valList = ['1', '2', '3']

# Iterating the elements in list
for val in valList:
	for ele in range(int(val), int(val) + 2):
		myDict.setdefault(ele, []).append(val)

print(myDict)
