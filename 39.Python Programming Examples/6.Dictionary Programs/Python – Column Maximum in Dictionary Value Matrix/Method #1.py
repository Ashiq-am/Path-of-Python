# Python3 code to demonstrate working of
# Column Maximums of Dictionary Value Matrix
# Using dictionary comprehension + sorted() + items()

# initializing dictionary
test_dict = {"Gfg" : [[5, 6], [3, 4]],
			"is" : [[4, 6], [6, 8]],
			"best" : [[7, 4], [2, 3]]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# sorted() used to sort and "-1" used to get last i.e
# maximum element
res = {key : sorted(val, key = lambda ele : (ele[0], ele[1]))[-1] for key, val in test_dict.items()}

# printing result
print("The evaluated dictionary : " + str(res))
