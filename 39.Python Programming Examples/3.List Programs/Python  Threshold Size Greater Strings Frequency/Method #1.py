# Python3 code to demonstrate working of
# Threshold Size Greater Strings Frequency
# using list comprehension + len()

# initialize list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# initialize K
K = 3

# Threshold Size Greater Strings Frequency
# using list comprehension + len()
res = len([ele for ele in test_list if len(ele) >= K])

# printing result
print("The frequency of threshhold K sized strings are : " + str(res))
