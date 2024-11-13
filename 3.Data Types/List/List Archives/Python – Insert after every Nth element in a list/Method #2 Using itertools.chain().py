# Python3 code to demonstrate
# inserting K after every Nth number
# using itertool.chain()
from itertools import chain

# initializing list
test_list = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r',
							'g', 'e', 'e', 'k', 's']

# printing original list
print ("The original list is : " + str(test_list))

# initializing k
k = 'x'

# initializing N
N = 3

# using itertool.chain()
# inserting K after every Nth number
res = list(chain(*[test_list[i : i+N] + [k]
			if len(test_list[i : i+N]) == N
			else test_list[i : i+N]
			for i in range(0, len(test_list), N)]))

# printing result
print ("The lists after insertion : " + str(res))
