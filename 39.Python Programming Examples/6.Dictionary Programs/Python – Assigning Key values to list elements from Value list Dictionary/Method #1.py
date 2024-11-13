# Python3 code to demonstrate working of
# Assigning Key values to list elements from Value list Dictionary
# Using list comprehension

# initializing list
test_list = [4, 6, 3, 10, 5, 3]

# printing original list
print("The original list : " + str(test_list))

# initializing dictionary
test_dict = {"Gfg" : [5, 3, 6], "is" : [8, 4], "Best" : [10, 11]}

# nested loop inside list comprehension to check each key
res = [key for ele in test_list
	for key, val in test_dict.items() if ele in val]

# printing result
print("The filtered list : " + str(res))
