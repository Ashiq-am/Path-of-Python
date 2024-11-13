# Python3 code to demonstrate working of
# Convert List of Dictionaries to List of Lists
# Using list comprehension

# initializing list
test_list = [{'Nikhil' : 17, 'Akash' : 18, 'Akshat' : 20},
			{'Nikhil' : 21, 'Akash' : 30, 'Akshat' : 10},
			{'Nikhil' : 31, 'Akash' : 12, 'Akshat' : 19}]

# printing original list
print("The original list is : " + str(test_list))

# Convert List of Dictionaries to List of Lists
# Using list comprehension
res = [[key for key in test_list[0].keys()], *[list(idx.values()) for idx in test_list ]]

# printing result
print("The converted list : " + str(res))
