# Python3 code to demonstrate
# index percentage calculation of element
# using loop + list comprehension

# initializing test list
test_list = [[3, 4, 5], [2, 4, 6], [3, 5, 4]]

# printing original list
print("The original list : " + str(test_list))

# using loop + list comprehension
# index percentage calculation of element
res = []
for i in range(len(test_list[1])):
	res.append(len([j[i] for j in test_list if j[i]== 4 ])/len(test_list))

# print result
print("The percentage of 4 each index is : " + str(res))
