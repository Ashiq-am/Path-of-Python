# Python3 code to demonstrate working of
# Values from custom List in Records
# Using list comprehension + itemgetter() + intersection()
from operator import itemgetter

# initializing list
test_list = [{'name' : 'Gfg', 'id' : 1, 'Score' : 3},
			{'name' : 'is', 'id' : 4, 'Score' : 10}]

# printing original list
print("The original list : " + str(test_list))

# initializing Get list
get_list = ['name', 'id']

# Values from custom List in Records
# Using list comprehension + itemgetter() + intersection()
res = [list(itemgetter(*set(get_list).intersection(idx))(idx)) for idx in test_list]

# printing result
print("All extracted values : " + str(res))
