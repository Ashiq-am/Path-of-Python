# Python3 code to demonstrate
# to insert one list in another
# using insert() + loop

# initializing lists
test_list = [4, 5, 6, 3, 9]
insert_list = [2, 3]

# initializing position
pos = 2

# printing original list
print ("The original list is : " + str(test_list))

# printing insert list
print ("The list to be inserted is : " + str(insert_list))

# using insert() + loop
# to insert one list in another
for i in range(len(insert_list)):
	test_list.insert(i + pos, insert_list[i])

# printing result
print ("The list after insertion is : " + str(test_list))
