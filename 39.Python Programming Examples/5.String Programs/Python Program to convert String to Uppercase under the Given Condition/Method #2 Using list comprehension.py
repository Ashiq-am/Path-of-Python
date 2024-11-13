# Python3 code to demonstrate working of
# Conditional Uppercase by size
# Using list comprehension

# initializing list
test_list = ["Gfg", "is", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# list comprehension for one liner solution
res = [ele.upper() if len(ele) > K else ele for ele in test_list]

# printing result
print("Modified Strings : " + str(res))
