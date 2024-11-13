# Python3 code to demonstrate working of
# Remove Keys from dictionary starting with K
# Using list comprehension + dict() + startswith() + items()

# initializing dictionary
test_dict = {"Apple" : 1, "Star" : 2, "App" : 4, "Gfg" : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing Substring
K = "Ap"

# Using list comprehension + dict() + startswith() + items()
# Remove Keys from dictionary starting with K
res = dict( [(x, y) for x, y in test_dict.items() if not x.startswith(K)] )

# printing result
print("Dictionary after key removal : " + str(res))
