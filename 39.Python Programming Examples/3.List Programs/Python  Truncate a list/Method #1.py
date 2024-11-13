# Python3 code to demonstrate
# to truncate list using pop()

# initializing list
test_list = [1, 4, 5, 6, 7, 3, 8, 9, 10]

# printing original list
print ("The original list is : " + str(test_list))

# size desired
k = 5

# using pop()
# to truncate list
n = len(test_list)
for i in range(0, n - k ):
	test_list.pop()

# printing result
print ("The truncated list is : " + str(test_list))
