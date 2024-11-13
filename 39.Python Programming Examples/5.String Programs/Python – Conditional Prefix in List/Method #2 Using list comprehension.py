# Python3 code to demonstrate working of
# Conditional Prefix in List
# Using list comprehension

# initializing list
test_list = [45, 53, 76, 86, 3, 49]

# printing original list
print("The original list : " + str(test_list))

# initializing pref 1
pref_1 = "LOW-"

# initializing pref 2
pref_2 = "HIGH-"

# solution encapsulated as one-liner and conditional checks
res = [pref_2 + str(ele) if ele >= 50 else pref_1 + str(ele) for ele in test_list]

# printing result
print("The prefixed elements : " + str(res))
