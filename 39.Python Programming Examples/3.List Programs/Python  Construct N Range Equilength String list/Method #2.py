# Python3 code to demonstrate working of
# Construct N Range Equilength String list
# using map() + string formatting

# initialize N
N = 6

# printing N
print("Number of elements required : " + str(N))

# initialize K
K = 3

# Construct N Range Equilength String list
# using map() + string formatting
temp = '{:0' + str(K) + '}'
res = list(map(temp.format, range(N)))

# printing result
print("K Length range strings list : " + str(res))
