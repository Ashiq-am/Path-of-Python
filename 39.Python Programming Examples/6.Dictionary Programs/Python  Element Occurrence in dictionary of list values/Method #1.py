# Python3 code to demonstrate
# Element Occurrence in dictionary value list
# using list comprehension + sum()

# initializing dictionary
test_dict = { "Akshat" : [1, 4, 5, 3],
			"Nikhil" : [4, 6],
			"Akash" : [5, 2, 1] }

# initializing test list
test_list = [2, 1]

# printing original dict
print("The original dictionary : " + str(test_dict))

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + sum()
# Element Occurrence in dictionary value list
res = {idx : sum(1 for i in j if i in test_list)
				for idx, j in test_dict.items()}

# print result
print("The summation of element occurrence : " + str(res))
