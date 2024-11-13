# Creating a dictionary
myDict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Using dictionary comprehension
for key in [key for key in myDict if key == 3]: del myDict[key]

# Modified Dictionary
print(myDict)
