# Python code to demonstrate how to remove
# an item from the dictionary without knowing
# a key using naive + del method

# Initialising dictionary
test1 = {"akshat": 21, "nikhil": 22, "akash": 23, "manjeet": 27}

# Printing dictionary before removal
print("Original Dictionary : " + str(test1))

# using naive + del method
# remove key nikhil
item_to_remove = 23

for key, item in test1.items():
    if item is item_to_remove:
        del test1[key]
        break

# Printing dictionary after removal
print("Dictionary after remove is : " + str(test1))
