# Python code to initialize a dictionary
# with only keys from a list

# List of Keys
keyList = ["Paras", "Jain", "Cyware"]

# Using Dictionary comprehension
myDict = {key: None for key in keyList}
print(myDict)
