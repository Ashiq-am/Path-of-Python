# Python3 code to demonstrate
# Similar Consecutive elements frequency
# using loop

# initializing list
test_list = [2, 2, 3, 3, 3, 3, 4, 4, 4]

# printing original list
print ("The original list is : " + str(test_list))

# Similar Consecutive elements frequency
# using loop
res = []
count = 1
for ele in range(0, len(test_list) -1):
	if test_list[ele] != test_list[ele + 1]:
		res.append((test_list[ele], count))
		count = 1
	else :
		count = count + 1
res.append((test_list[len(test_list) -1], count))

# printing result
print ("The consecutive element frequency is : " + str(res))
