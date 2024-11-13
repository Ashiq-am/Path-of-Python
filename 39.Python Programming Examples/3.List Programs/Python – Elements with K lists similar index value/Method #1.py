# Python3 code to demonstrate
# Elements with K lists similar index value
# using zip() + loop

# Initializing lists
test_list1 = [1, 3, 5, 7]
test_list2 = [1, 4, 8, 9]
test_list3 = [3, 7, 5, 10]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))
print("The original list 3 is : " + str(test_list3))

# Initializing K
K = 2

# Elements with K lists similar index value
# using zip() + loop
res = []
for a, b, c in zip(test_list1, test_list2, test_list3):
	if a == b or b == c or c == a:
		if a == b:
			res.append(a)
		elif b == c:
			res.append(b)
		elif c == a:
			res.append(c)

# printing result
print ("The list after checking on 2 lists : " + str(res))
