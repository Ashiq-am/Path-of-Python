# Creating a dictionary
myDict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Using dictionary comprehension to find list
# keys having value in 3.
delete = [key for key in myDict if key == 3]

# delete the key
for key in delete: del myDict[key]

# Modified Dictionary
print(myDict)
