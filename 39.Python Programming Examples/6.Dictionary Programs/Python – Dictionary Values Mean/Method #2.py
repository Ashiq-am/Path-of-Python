# Python3 code to demonstrate working of
# Dictionary Values Mean
# Using sum() + len() + values()

# initializing dictionary
test_dict = {"Gfg" : 4, "is" : 7, "Best" : 8, "for" : 6, "Geeks" : 10}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# values extracted using values()
# one-liner solution to problem.
res = sum(test_dict.values()) / len(test_dict)

# printing result
print("The computed mean : " + str(res))
