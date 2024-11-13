# Python3 code to demonstrate working of
# Minimum K records of Nth index in tuple list
# Using groupby() + sorted() + loop
import itertools

# initialize list
test_list = [('gfg', 4, 'good'), ('gfg', 2, 'better'),
			('gfg', 1, 'best'), ('gfg', 3, 'geeks')]

# printing original list
print("The original list is : " + str(test_list))

# initialize N
N = 1

# initialize K
K = 2

# Minimum K records of Nth index in tuple list
# Using groupby() + sorted() + loop
res = []
temp = itertools.groupby(sorted(test_list, key = lambda sub : sub[N]),
											key = lambda sub : sub[N])

for i in range(K):
	res.extend(list(next(temp)[N]))

# printing result
print("Min K elements of Nth index are : " + str(res))
