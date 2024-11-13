# Python3 code to demonstrate working of
# Next N elements of K value
# Using filter() + lambda + loop

# initializing list
test_list = [3, 4, 6, 7, 8, 4, 7, 2, 1, 8, 4, 2, 3, 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

# initializing N
N = 2

# getting indices of K
# using filter() and lambda
temp = list(filter(lambda ele: test_list[ele] == K, range(len(test_list))))

# getting next N elements from K using loop
res = []
for ele in temp:

	# appending slice
	res.extend(test_list[ele + 1: ele + N + 1])

# printing result
print("Constructed Result List : " + str(res))
