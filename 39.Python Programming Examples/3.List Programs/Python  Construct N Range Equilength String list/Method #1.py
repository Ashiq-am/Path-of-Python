# Python3 code to demonstrate working of
# Construct N Range Equilength String list
# using list comprehension + zfill()

# initialize N
N = 6

# printing N
print("Number of elements required : " + str(N))

# initialize K
K = 3

# Construct N Range Equilength String list
# using list comprehension + zfill()
res = [str(ele).zfill(K) for ele in range(N)]

# printing result
print("K Length range strings list : " + str(res))
