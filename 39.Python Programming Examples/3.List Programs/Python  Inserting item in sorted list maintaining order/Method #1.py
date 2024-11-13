# Python3 code to demonstrate
# insertion in sorted list
# using naive method

# initializing list
test_list = [1, 2, 3, 6, 7]

# printing original list
print ("The original list is : " + str(test_list))

# insert element
k = 5

# using naive method
# insertion in sorted list
# using naive method
for i in range(len(test_list)):
	if test_list[i] > k:
		index = i
		break
res = test_list[: i] + [k] + test_list[i :]

# printing result
print ("The list after insertion is : " + str(res))
