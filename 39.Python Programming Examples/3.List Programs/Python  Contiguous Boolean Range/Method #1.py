# Python3 code to demonstrate
# Contiguous Boolean Ranging
# using enumerate() + zip() + list comprehension

# initializing list
test_list = [True, True, False, False, True,
			True, True, True, False, True]

# printing the original list
print ("The original list is : " + str(test_list))

# using enumerate() + zip() + list comprehension
# for Contiguous Boolean Ranging
res = [x for x, (i , j) in enumerate(zip( [2]
		+ test_list, test_list + [2])) if i != j]

# printing result
print ("The boolean range list is : " + str(res))
