# Python3 code to demonstrate
# divide list to siblist on deliminator
# using itertools.groupby() + list comprehension
from itertools import groupby

# initializing list
test_list = ['Geeks', '', 'for', '', 4, 5, '',
				'Geeks', 'CS', '', 'Portal']

# printing original list
print("The original list : " + str(test_list))

# using itertools.groupby() + list comprehension
# divide list to siblist on deliminator
res = [list(sub) for ele, sub in groupby(test_list, key = bool) if ele]

# print result
print("The list of sublist after separation : " + str(res))
