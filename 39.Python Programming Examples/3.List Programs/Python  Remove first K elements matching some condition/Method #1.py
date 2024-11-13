# Python3 code to demonstrate
# to remove first K elements matching condition
# using Naive Method

# initializing list
test_list = [3, 5, 1, 6, 7, 9, 8, 5]

# printing original list
print ("The original list is : " + str(test_list))

# using Naive Method
# to remove first K elements matching condition
# removes first 4 odd occurrences
counter = 1
res = []
for i in test_list:
	if counter > 4 or not (i % 2 != 0):
		res.append(i)
	else:
		counter += 1

# printing result
print ("The filtered list is : " + str(res))
