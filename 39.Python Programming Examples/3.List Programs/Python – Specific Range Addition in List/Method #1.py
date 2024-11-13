# Python3 code to demonstrate
# Specific Range Addition in List
# using loop

# Initializing list
test_list = [4, 5, 6, 8, 10, 11]

# printing original list
print("The original list is : " + str(test_list))

# Initializing range
i, j = 2, 5

# Specific Range Addition in List
# using loop
for idx in range(i, j):
	test_list[idx] += 3

# printing result
print ("List after range addition : " + str(test_list))
