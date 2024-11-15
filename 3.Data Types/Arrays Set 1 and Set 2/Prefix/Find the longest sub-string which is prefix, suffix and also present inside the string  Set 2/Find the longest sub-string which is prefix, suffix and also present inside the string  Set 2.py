# Python3 program to find that
# substring which is its
# suffix prefix and also
# found somewhere in between

# Z-algorithm function
def z_function(s):
	global z, n
	n = len(s)
	z = [0] * n
	l, r = 0, 0
	for i in range(1, n):
		if i <= r:
			z[i] = min(r - i + 1, z[i - 1])

		while (i + z[i] < n and s[z[i]] == s[i + z[i]]):
			z[i] += 1

		if (i + z[i] - 1 > r):
			l = i
			r = i + z[i] - 1
	return z

# bit update function which
# updates values from index
# "idx" to last by value "val"
def update(idx, val):
	global bit
	if idx == 0:
		return
	while idx <= n:
		bit[idx] += val
		idx += (idx & -idx)

# Query function in bit
def pref(idx):
	global bit
	ans = 0
	while idx > 0:
		ans += bit[idx]
		idx -= (idx & -idx)

	return ans

# Driver Code
if __name__ == "__main__":
	n = 0
	length = 0

	# BIT array
	bit = [0] * 1000005
	z = []
	m = dict()

	s = "geeksisforgeeksinplatformgeeks"

	# Making the z array
	z = z_function(s)

	# update in the bit array from
	# index z[i] by increment of 1
	for i in range(1, n):
		update(z[i], 1)

	for i in range(n - 1, 1, -1):

		# if the value in z[i] is
		# not equal to (n-i) then no
		# need to move further
		if z[i] != n - i:
			continue

		# queryng for the maximum
		# length substring from
		# bit array
		if (pref(n) - pref(z[i] - 1)) >= 2:
			length = max(length, z[i])

	if not length:
		print(-1)
	else:
		print(s[:length])

# This code is contributed by
# sanjeev2552
