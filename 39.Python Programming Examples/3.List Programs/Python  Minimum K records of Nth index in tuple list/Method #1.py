# Python3 code to demonstrate working of
# Minimum K records of Nth index in tuple list
# Using filter() + lambda + set() + list comprehension

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
# Using filter() + lambda + set() + list comprehension
temp = set(list({sub[N] for sub in test_list})[ :K])
res = list(filter(lambda sub: sub[N] in temp, test_list))

# printing result
print("Min K elements of Nth index are : " + str(res))
