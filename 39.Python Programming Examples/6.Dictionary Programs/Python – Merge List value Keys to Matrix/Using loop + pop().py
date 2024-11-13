# Python3 code to demonstrate working of
# Merge List value Keys to Matrix
# Using loop + pop()

# initializing dictionary
test_dict = {'gfg' : [4, 5, 6],
			'is' : [8, 8, 9],
			'CS' : [1, 3, 8],
			'Maths' : [1, 2]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing list
que_list = ['gfg', 'CS', 'Maths']

# Merge List value Keys to Matrix
# Using loop + pop()
new_data = [test_dict.pop(ele) for ele in que_list]
test_dict["merge_key"] = new_data

# printing result
print("The dictionary after merging : " + str(test_dict))
