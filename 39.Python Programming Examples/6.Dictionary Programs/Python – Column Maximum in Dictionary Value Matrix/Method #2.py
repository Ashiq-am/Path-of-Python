# Python3 code to demonstrate working of
# Column Maximums of Dictionary Value Matrix
# Using max() + map() + zip()

# initializing dictionary
test_dict = {"Gfg" : [[5, 6], [3, 4]],
			"is" : [[4, 6], [6, 8]],
			"best" : [[7, 4], [2, 3]]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# map extending logic to entire columns
# result compiled using dictionary comprehension
res = {key: list(map(max, zip(*val))) for key, val in test_dict.items()}

# printing result
print("The evaluated dictionary : " + str(res))
