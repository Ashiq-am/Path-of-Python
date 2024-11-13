# Python3 code to demonstrate
# Incremental K sized Row Matrix Initialization
# using loop + list slicing

# Initialization of row size
K = 3

# Incremental K sized Row Matrix Initialization
# using loop + list slicing
res = []
for idx in range(1, 10, K):
	sub = [idx, idx + 1, idx + 2]
	res.append(sub)

# printing result
print ("The Incremental Initialized Matrix is : " + str(res))
