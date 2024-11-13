# Python3 code to demonstrate working of
# Pair summation of list
# Using loop

# initializing list
test_list = [4, 5, 8, 9, 10, 17]

# printing list
print("The original list : " + str(test_list))

# Pair summation of list
# Using loop
res = []
for ele in range(0, len(test_list), 2):
	res.append(test_list[ele] + test_list[ele + 1])

# Printing result
print("Pair summation of list : " + str(res))
