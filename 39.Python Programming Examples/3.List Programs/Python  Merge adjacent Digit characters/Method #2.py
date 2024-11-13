# Python3 code to demonstrate
# Merge adjacent Digit characters
# itertools.chain.from_iterable() + groupby() + join()
from itertools import chain, groupby

# initializing list
test_list = ['Geeks', 'for', 'Geeks', '2', '5']

# printing original list
print("The original list : " + str(test_list))

# using itertools.chain.from_iterable() + groupby() + join()
# Merge adjacent Digit characters
num_group = groupby(test_list, key = str.isdigit)
both_group = [[''.join(i)] if j else list(i) for j, i in num_group]
res = list(chain.from_iterable(both_group))

# print result
print("The joined adjacent word list(ignoring alphabets) : " + str(res))
