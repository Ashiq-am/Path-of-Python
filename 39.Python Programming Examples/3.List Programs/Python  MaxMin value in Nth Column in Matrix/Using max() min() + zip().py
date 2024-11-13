# Python3 code to demonstrate working of
# Max value in Nth Column in Matrix
# using max() + zip()

# initialize list
test_list = [[5, 6, 7],
			[9, 10, 2],
			[10, 3, 4]]

# printing original list
print("The original list is : " + str(test_list))

# initialize N
N = 2

# Max value in Nth Column in Matrix
# using max() + zip()
res = [max(i) for i in zip(*test_list)][N]

# printing result
print("Max value of Nth column is : " + str(res))
