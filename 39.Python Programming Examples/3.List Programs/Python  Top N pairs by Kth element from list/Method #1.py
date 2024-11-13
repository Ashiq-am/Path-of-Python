# Python3 code to demonstrate working of
# Top N pairs by Kth element from list
# Using filter() + lambda + set() + list comprehension

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
# Using filter() + lambda + set() + list comprehension
temp = set(list({sub[K] for sub in test_list})[-N:])
res = list(filter(lambda sub: sub[K] in temp, test_list))

# printing result
print("Top N elements of Kth index are : " + str(res))
