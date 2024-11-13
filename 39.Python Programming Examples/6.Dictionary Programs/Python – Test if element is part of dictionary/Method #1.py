# Python3 code to demonstrate working of
# Test if element is part of dictionary
# Using any() + generator expression + items()

# initializing dictionary
test_dict = {"Gfg" : 1, "is" : 3, "Best" : 2}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = "Gfg"

# using any() to check for both keys and values
res = any(K == key or K == val for key, val in test_dict.items())

# printing result
print("Is K present in dictionary? : " + str(res))
