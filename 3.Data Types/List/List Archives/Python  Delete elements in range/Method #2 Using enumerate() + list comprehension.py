# Python3 code to demonstrate
# range deletion of elements
# using enumerate() + list comprehension

# initializing list
test_list = [3, 5, 6, 7, 2, 10]

# initializing indices
indices_list = [1, 4, 2]

# printing the original list
print ("The original list is : " + str(test_list))

# printing the indices list
print ("The indices list is : " + str(indices_list))

# using enumerate() + list comprehension
# range deletion of elements
test_list[:] = [ j for i, j in enumerate(test_list)
						if i not in indices_list ]

# printing result
print ("The modified deleted list is : " + str(test_list))
