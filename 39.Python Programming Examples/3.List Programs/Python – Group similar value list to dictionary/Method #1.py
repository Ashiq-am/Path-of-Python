# Python3 code to demonstrate
# Group similar value list to dictionary
# using dictionary comprehension

# Initializing lists
test_list1 = [4, 4, 4, 5, 5, 6, 6, 6, 6]
test_list2 = ['G', 'f', 'g', 'i', 's', 'b', 'e', 's', 't']

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Group similar value list to dictionary
# using dictionary comprehension
res = {key : [test_list2[idx]
	for idx in range(len(test_list2)) if test_list1[idx]== key]
	for key in set(test_list1)}

# printing result
print ("Mapped resultant dictionary : " + str(res))
