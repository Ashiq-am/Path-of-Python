# Python3 code to demonstrate
# similarity between strings
# using naive method (sum() + zip())

# Utility function to compute similarity
def similar(str1, str2):
	str1 = str1 + ' ' * (len(str2) - len(str1))
	str2 = str2 + ' ' * (len(str1) - len(str2))
	return sum(1 if i == j else 0
			for i, j in zip(str1, str2)) / float(len(str1))

# Initializing strings
test_string1 = 'Geeksforgeeks'
test_string2 = 'Geeks4geeks'

# using naive method (sum() + zip())
# similarity between strings
res = similar(test_string1, test_string2)

# printing the result
print ("The similarity between 2 strings is : " + str(res))
