# Python 3 code to demonstrate
# Summation of first N matching condition
# using Naive Method

# initializing list
test_list = [3, 5, 1, 6, 7, 9, 8, 5]

# printing original list
print ("The original list is : " + str(test_list))

# using Naive Method
# Summation of first N matching condition
# sums first 3 odd occurrences
counter = 1
res = 0
for i in test_list:
	if counter <= 3 and (i % 2 != 0):
		res = res + i
		counter = counter + 1

# printing result
print ("The filtered list is : " + str(res))
