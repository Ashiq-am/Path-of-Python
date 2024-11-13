# Python3 code to demonstrate
# joining only adjacent words in list
# itertools.chain.from_iterable() + groupby() + join()
from itertools import chain, groupby

# initializing list
test_list = ['Geeks', '5', 'for', 'Geeks' , '2', '3']

# printing original list
print("The original list : " + str(test_list))

# using itertools.chain.from_iterable() + groupby() + join()
# joining only adjacent words in list
num_group = groupby(test_list, key = str.isalpha)
both_group = [[''.join(i)] if j else list(i)
					for j, i in num_group]

res = list(chain.from_iterable(both_group))

# print result
print("The joined adjacent word list(ignoring digits) : "
											+ str(res))
