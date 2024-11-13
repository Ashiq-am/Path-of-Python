# Python3 code to demonstrate working of
# Sort by Factor count
# Using lambda + sorted() + len()

# initializing list
test_list = [12, 100, 360, 22, 200]

# printing original list
print("The original list is : " + str(test_list))

# performing sort using sorted(), lambda getting factors
res = sorted(test_list, key=lambda ele: len(
	[ele for idx in range(1, ele) if ele % idx == 0]))

# printing result
print("Sorted List : " + str(res))
