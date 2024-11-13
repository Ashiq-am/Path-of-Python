# Python3 code to demonstrate working of
# Filter above Threshold size Strings
# using list comprehension + len()

# initialize list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# initialize Threshold
thres = 4

# Filter above Threshold size Strings
# using list comprehension + len()
res = [ele for ele in test_list if len(ele) >= thres]

# printing result
print("The above Threshold size strings are : " + str(res))
