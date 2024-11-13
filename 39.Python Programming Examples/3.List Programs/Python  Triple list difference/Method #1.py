# Python3 code to demonstrate
# triple list difference
# using map() + set() + list comprehension

# initializing lists
test_list1 = [1, 5, 6, 4, 7]
test_list2 = [8, 4, 3]
test_list3 = [9, 10, 3, 5]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))
print("The original list 3 : " + str(test_list3))

# using map() + set() + list comprehension
# triple list difference
temp1, temp2, temp3 = map(set, (test_list1, test_list2, test_list3))
res1 = [ele for ele in test_list1 if ele not in temp2 and ele not in temp3]
res2 = [ele for ele in test_list2 if ele not in temp1 and ele not in temp3]
res3 = [ele for ele in test_list3 if ele not in temp2 and ele not in temp1]

# print result
print("The mutual difference list are : "
	+ str(res1) + " " + str(res2) + " " + str(res3))
