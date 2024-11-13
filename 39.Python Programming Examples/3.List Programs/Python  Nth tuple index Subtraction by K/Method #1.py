# Python3 code to demonstrate working of
# Nth tuple element Subtraction by K
# Using loop

# Initializing list
test_list = [(4, 5, 6), (7, 4, 2), (9, 10, 11)]

# printing original list
print("The original list is : " + str(test_list))

# Initializing N
N = 1

# Initializing K
K = 3

# Nth tuple element Subtraction by K
# Using loop
res = []
for i in range(0, len(test_list)):
	res.append((test_list[i][0], test_list[i][N] - K, test_list[i][2]))

# printing result
print("The tuple after removing K from Nth element : " + str(res))
