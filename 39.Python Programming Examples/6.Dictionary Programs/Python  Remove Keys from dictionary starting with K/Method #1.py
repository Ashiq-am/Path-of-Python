# Python3 code to demonstrate working of
# Remove Keys from dictionary starting with K
# Using Naive Method + startswith() + pop()

# initializing dictionary
test_dict = {"Apple" : 1, "Star" : 2, "App" : 4, "Gfg" : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing Substring
K = "Ap"

# Using Naive Method + startswith() + pop()
# Remove Keys from dictionary starting with K
res = list(test_dict.keys())
for key in res:
    if key.startswith(K):
        test_dict.pop(key)

# printing result
print("Dictionary after key removal : " + str(test_dict))
