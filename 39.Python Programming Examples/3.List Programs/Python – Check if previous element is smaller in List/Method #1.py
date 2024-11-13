# Python3 code to demonstrate working of
# Check if previous element is smaller in List
# Using loop

# initializing list
test_list = [6, 3, 7, 3, 6, 7, 8, 3]

# printing original list
print("The original list is : " + str(test_list))

# Check if previous element is smaller in List
# Using loop
res = []
for idx in range(1, len(test_list)):
	if test_list[idx - 1] < test_list[idx]:
		res.append(True)
	else:
		res.append(False)

# printing result
print("List after filtering : " + str(res))
