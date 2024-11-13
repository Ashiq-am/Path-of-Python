# Python code to demonstrate
# to test all elements in list are unique
# using Counter.itervalues()
from collections import Counter

# initializing list
test_list = [1, 3, 4, 6, 7]

# printing original list
print ("The original list is : " + str(test_list))

flag = 0

# using Counter.itervalues()
# to check all unique list elements
counter = Counter(test_list)
for values in counter.itervalues():
		if values > 1:
			flag = 1


# printing result
if(not flag) :
	print ("List contains all unique elements")
else :
	print ("List contains does not contains all unique elements")
