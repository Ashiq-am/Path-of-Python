# Python3 code to demonstrate working of
# Alternate elements Similarity
# Using loop

# initializing lists
test_list = [5, 3, 5, 2, 5, 8, 5]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 5

# using flag to Flag false if any one element is not K
# using loop to check for each element
res = True
for idx, ele in enumerate(test_list):
	if not idx % 2 and ele != K:
		res = False
		break

# printing result
print("Are all alternate elements equal to K : " + str(res))
