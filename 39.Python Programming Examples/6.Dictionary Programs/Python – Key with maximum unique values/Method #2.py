# Python3 code to demonstrate working of
# Key with maximum unique values
# Using sorted() + lambda() + set() + values() + len()

# initializing dictionary
test_dict = {"Gfg" : [5, 7, 5, 4, 5],
			"is" : [6, 7, 4, 3, 3],
			"Best" : [9, 9, 6, 5, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# one-liner to solve a problem
# sorted used to reverse sort dictionary
max_key = sorted(test_dict, key = lambda ele: len(
		set(test_dict[ele])), reverse = True)[0]

# printing result
print("Key with maximum unique values : " + str(max_key))
