# Python3 code to demonstrate working of
# Convert Lists to column tuples
# using zip() + list comprehension

# initialize dictionary
test_dict = {'list1' : [1, 4, 5],
			'list2' : [6, 7, 4],
			'list3' : [9, 1, 11]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert Lists to column tuples
# using zip() + list comprehension
res = list(zip(*(test_dict[key] for key in test_dict.keys())))

# printing result
print("Like index column tuples are : " + str(res))
