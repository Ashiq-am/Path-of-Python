# Python3 code to demonstrate
# to compute all possible permutations
# using list comprehension

# initializing lists
list1 = [1, 3, 4]
list2 = [6, 7, 9]
list3 = [8, 10, 5]

# printing lists
print ("The original lists are : " + str(list1) +
							" " + str(list2) +
							" " + str(list3))

# using list comprehension
# to compute all possible permutations
res = [[i, j, k] for i in list1
				for j in list2
				for k in list3]

# printing result
print ("All possible permutations are : " + str(res))
