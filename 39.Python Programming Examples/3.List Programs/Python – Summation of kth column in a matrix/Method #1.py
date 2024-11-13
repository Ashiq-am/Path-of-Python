# Python3 code to demonstrate working of
# Matrix Kth column summation
# using sum() + zip()

# initialize list
test_list = [[5, 6, 7],
			[9, 10, 2],
			[10, 3, 4]]

# printing original list
print("The original list is : " + str(test_list))

# initialize K
K = 2

# Matrix Kth column summation
# using sum() + zip()
res = [sum(idx) for idx in zip(*test_list)][K]

# printing result
print("Sum of Kth column is : " + str(res))
