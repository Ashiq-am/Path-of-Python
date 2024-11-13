# Python3 code to demonstrate working of
# Resize Keys in dictionary
# Using dictionary comprehension + slicing

# initializing dictionary
test_dict = {"geeksforgeeks": 3, "best": 3, "coding": 4, "practice": 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 2

# reforming dictionary
res = {key[:K]: test_dict[key] for key in test_dict}

# printing result
print("The required result : " + str(res))
