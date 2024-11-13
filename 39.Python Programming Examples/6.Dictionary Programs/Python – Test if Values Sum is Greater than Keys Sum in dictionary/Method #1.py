# Python3 code to demonstrate working of
# Test if Values Sum is Greater than Keys Sum in dictionary
# Using loop

# initializing dictionary
test_dict = {5: 3, 1: 3, 10: 4, 7: 3, 8: 1, 9: 5}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

key_sum = 0
val_sum = 0

for key in test_dict:

	# getting sum
	key_sum += key
	val_sum += test_dict[key]

# checking if val_sum greater than key sum
res = val_sum > key_sum

# printing result
print("The required result : " + str(res))
