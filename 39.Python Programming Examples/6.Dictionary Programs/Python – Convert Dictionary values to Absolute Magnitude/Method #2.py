# Python3 code to demonstrate working of
# Convert Dictionary values to Absolute Magnitude
# Using dictionary comprehension + abs()

# initializing dictionary
test_dict = {"Gfg" : 5, "is" : -7, "Best" : 2, "for" : -9, "geeks" : -8}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# dictionary comprehension using to compile result
# items() used to extract dictionary keys and values.
res = {key : abs(val) for key, val in test_dict.items()}

# printing result
print("Dictionary after absulute conversion : " + str(res))
