# Python3 code to demonstrate working of
# List consecutive pair Product
# Using loop

# initializing list
test_list = [5, 8, 3, 5, 9, 10]

# printing list
print("The original list : " + str(test_list))

# List consecutive pair Product
# Using loop
res = []
for ele in range(0, len(test_list), 2):
	res.append(test_list[ele] * test_list[ele + 1])

# Printing result
print("Pair product of list : " + str(res))
