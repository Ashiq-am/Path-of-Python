# Python3 code to demonstrate
# Vertical list print
# using zip()

# initializing list
test_list = [[1, 4, 5], [4, 6, 8], [8, 3, 10]]

# printing original list
print ("The original list is : " + str(test_list))

# using zip()
# to print list vertically
for x, y, z in zip(*test_list):
	print(x, y, z)
