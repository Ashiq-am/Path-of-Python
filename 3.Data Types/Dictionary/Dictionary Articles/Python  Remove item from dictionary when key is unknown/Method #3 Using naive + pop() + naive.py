# Python code to demonstrate how to remove
# item from dictionary without knowing key
# using naive + pop()

# Initialising dictionary
test1 = {"akshat": 21, "nikhil": 22, "akash": 23, "manjeet": 27}

# Printing dictionary before removal
print("Original dictionary : " + str(test1))

# using naive + pop()
# remove key akash
value_to_remove = 23

for key in test1.keys():
    if test1[key] == value_to_remove:
        test1.pop(key)
        break

# Printing dictionary after removal
print("Dictionary after remove is : " + str(test1))
