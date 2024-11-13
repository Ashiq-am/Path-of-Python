# Python3 code to demonstrate
# to perform cyclic initialization
# using list comprehension

# count of 1
count_1 = 4

# count of 0
count_0 = 3

# total length of list
size = 14

# initializing list cyclically
# using list comprehension
test_list = [ 1 if i % (count_1 + count_0) < count_1
				else 0 for i in range(size) ]

# printing list after change
print ("The list after initializing : " + str(test_list))
