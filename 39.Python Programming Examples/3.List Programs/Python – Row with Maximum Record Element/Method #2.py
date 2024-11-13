# Python3 code to demonstrate working of
# Row with Maximum Record Element
# Using max() + itemgetter()
from operator import itemgetter

# initializing list
test_list = [[(12, 4), (6, 7)],
			[(15, 2), (19, 3)],
			[(18, 3), (12, 4)],
			[(17, 1), (11, 3)]]

# printing original list
print("The original list is : " + str(test_list))

# Row with Maximum Record Element
# Using max() + itemgetter()
res = max(test_list, key = itemgetter(1))

# printing result
print("The row with Maximum Value : " + str(res))
