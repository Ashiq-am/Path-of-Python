# Python3 code to demonstrate
# Alternate front - rear Sum
# using loop

# initializing list
test_list = [1, 4, 5, 3, 6, 7]

# printing original list
print ("The original list is : " + str(test_list))

# Alternate front - rear Sum
# using loop
res = []
j = len(test_list) - 1
for i in range(0, len(test_list) // 2):
	res.append(test_list[i] + test_list[j])
	j = j - 1

# printing result
print ("The alterate front - rear Sum list is : " + str(res))
