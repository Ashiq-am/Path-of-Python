# Python3 code to demonstrate working of
# Convert Dictionary values to Absolute Magnitude
# Using loop + abs()

# initializing dictionary
test_dict = {"Gfg" : 5, "is" : -7, "Best" : 2, "for" : -9, "geeks" : -8}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using abs() to perform conversion
# from negative to positive values
for ele in test_dict:
	test_dict[ele] = abs(test_dict[ele])

# printing result
print("Dictionary after absulute conversion : " + str(test_dict))
