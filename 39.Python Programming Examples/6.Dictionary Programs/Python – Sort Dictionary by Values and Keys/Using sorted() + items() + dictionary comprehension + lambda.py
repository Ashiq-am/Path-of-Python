# Python3 code to demonstrate working of
# Sort Dictionary by Values and Keys
# Using sorted() + items() + dictionary comprehension + lambda

# initializing dictionary
test_dict = {"Gfg" : 1, "is" : 3, "Best" : 2, "for" : 3, "Geeks" : 2}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# - sign for descended values, omit if low-high sorting required
res = {val[0] : val[1] for val in sorted(test_dict.items(), key = lambda x: (-x[1], x[0]))}

# printing result
print("Sorted dictionary : " + str(res))
