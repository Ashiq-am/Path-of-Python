# Python3 code to demonstrate working of
# Aggregate values by tuple keys
# using groupby() + map() + itemgetter() + sum()
from itertools import groupby
from operator import itemgetter

# initialize list
test_list = [('gfg', 50), ('is', 30), ('best', 100),
						('gfg', 20), ('best', 50)]

# printing original list
print("The original list is : " + str(test_list))

# Aggregate values by tuple keys
# using groupby() + map() + itemgetter() + sum()
res = [(key, sum(map(itemgetter(1), ele)))
	for key, ele in groupby(sorted(test_list, key = itemgetter(0)),
												key = itemgetter(0))]

# printing result
print("List after grouping : " + str(res))
