# Python code to demonstrate how to remove
# item from dictionary without knowing key
# using dictionary comprehension

# Initialising dictionary
test1 = {"akshat": 21, "nikhil": 22, "akash": 23, "manjeet": 27}

# Printing dictionary before removal
print("Original Dictionary : " + str(test1))

# using dictionary comprehension method
# remove key akash
value_to_remove = 23

res = {key: value for key, value in test1.items()
       if value is not value_to_remove}

# Printing dictionary after removal
print("Dictionary after remove is : " + str(res))
