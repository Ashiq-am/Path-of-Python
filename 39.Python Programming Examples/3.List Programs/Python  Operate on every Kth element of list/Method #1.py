# Python3 code to demonstrate
# Edit every Kth element in list
# using list comprehension + enumerate()

# initializing list
test_list = [1, 4, 5, 6, 7, 8, 9, 12]

# printing the original list
print ("The original list is : " + str(test_list))

# using list comprehension + enumerate()
# Edit every Kth element in list
# add 2 to every 3rd element
res = [i + 2 if j % 3 == 0 else i
	for j, i in enumerate(test_list)]

# printing result
print ("The list after editing every kth element : " + str(res))
