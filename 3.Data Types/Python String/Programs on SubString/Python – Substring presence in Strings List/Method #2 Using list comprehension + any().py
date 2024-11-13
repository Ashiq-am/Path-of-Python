# Python3 code to demonstrate working of
# Substring presence in Strings List
# Using list comprehension + any()

# initializing lists
test_list1 = ["Gfg", "is", "Best"]
test_list2 = ["I love Gfg", "Its Best for Geeks", "Gfg means CS"]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# any() reduces a nesting
# checks for element presence in all Substrings
res = [True if any(i in j for j in test_list2) else False for i in test_list1]

# printing result
print("The match list : " + str(res))
