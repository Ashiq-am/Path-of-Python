# Python3 code to demonstrate
# triple list difference
# using map() + set() + "-" operator

# initializing lists
test_list1 = [1, 5, 6, 4, 7]
test_list2 = [8, 4, 3]
test_list3 = [9, 10, 3, 5]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))
print("The original list 3 : " + str(test_list3))

# using map() + set() + "-" operator
# triple list difference
temp1, temp2, temp3 = map(set, (test_list1, test_list2, test_list3))
res1 = temp1 - temp2 - temp3
res2 = temp2 - temp3 - temp1
res3 = temp3 - temp1 - temp2
res1, res2, res3 = map(list, (res1, res2, res3))

# print result
print("The mutual difference list are : "
	+ str(res1) + " " + str(res2) + " " + str(res3))
