# Python3 code to demonstrate
# cyclic iteration in list
# using % operator and loop

# initializing tuple list
test_list = [5, 4, 2, 3, 7]

# printing original list
print ("The original list is : " + str(test_list))

# starting index
K = 3

# using % operator and loop
# cyclic iteration in list
res = []
for i in range(len(test_list)):
	res.append(test_list[K % len(test_list)])
	K = K + 1

# printing result
print ("The cycled list is : " + str(res))
