# Python3 code to demonstrate
# Diagonal element addition among lists
# using loop

# Initializing lists
test_list1 = [1, 6, 8, 5, 3]
test_list2 = [8, 10, 3, 4, 5]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Diagonal element addition among lists
# using loop
res = []
for idx in range(0, len(test_list1) - 1):
	res.append(test_list1[idx] + test_list2[idx + 1])

# printing result
print ("List after diagonal addition : " + str(res))
