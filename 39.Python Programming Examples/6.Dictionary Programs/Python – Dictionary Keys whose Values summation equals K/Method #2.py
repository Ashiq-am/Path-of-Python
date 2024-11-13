# Python3 code to demonstrate working of
# Dictionary Keys whose Values summation equals K
# Using list comprehension

# initializing dictionary
test_dict = {"Gfg" : 3, "is" : 5, "Best" : 9, "for" : 8, "Geeks" : 10}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 14

# extracting keys and values
keys = list(test_dict.keys())
values = list(test_dict.values())

# checking for keys in one liner
res = [[keys[i], keys[j]] for i in range(len(keys)) for j in range(i + 1, len(keys)) if values[i] + values[j] == K]

# printing result
print("Keys whose sum equals K : " + str(res))
