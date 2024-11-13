# Creating a dictionary
myDict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# list of delete keys
delete = []
for key, val in myDict.items():
    if val == 'Geeks':
        delete.append(key)

for i in delete:
    del myDict[i]

# Modified Dictionary
print(myDict)
