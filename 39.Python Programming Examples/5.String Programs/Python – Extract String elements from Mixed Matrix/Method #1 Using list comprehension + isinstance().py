# Python3 code to demonstrate working of
# Extract String elements from Mixed Matrix
# Using list comprehension + isinstance()

# initializing lists
test_list = [[5, 6, 3], ["Gfg", 3, "is"], [9, "best", 4]]

# printing original list
print("The original list : " + str(test_list))

# strings are extracted using isinstance()
res = [ele for sub in test_list for ele in sub if isinstance(ele, str)]

# printing result
print("The String instances : " + str(res))
