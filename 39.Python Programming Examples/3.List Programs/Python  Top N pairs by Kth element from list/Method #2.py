# Python3 code to demonstrate working of
# Top N pairs by Kth element from list
# Using groupby() + sorted() + loop
import itertools

# initialize list
test_list = [('gfg', 4, 'good'), ('gfg', 2, 'better'),
			('gfg', 1, 'best'), ('gfg', 3, 'geeks')]

# printing original list
print("The original list is : " + str(test_list))

# initialize N
N = 3

# initialize K
K = 1

# Top N pairs by Kth element from list
# Using groupby() + sorted() + loop
res = []
temp = itertools.groupby(sorted(test_list, key = lambda sub : sub[K],
						reverse = True), key = lambda sub : sub[K])
for i in range(N):
	res.extend(list(next(temp)[K]))

# printing result
print("Top N elements of Kth index are : " + str(res))
