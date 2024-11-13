# Python3 program to count the
# number of numbers in range
# 1-M that are divisible by
# given N prime numbers


def bitsoncount(x):
	return bin(x).count('1')

# function to count the number
# of numbers in range 1-M that
# are divisible by given N
# prime numbers


def count(a, m, n):

	odd = 0
	even = 0
	p = 1
	pow_set_size = 1 << n

	# Run from counter 000..0 to 111..1
	for counter in range(1, pow_set_size):

		p = 1
		for j in range(n):

			# Check if jth bit in the
			# counter is set If set
			# then pront jth element from set
			if (counter & (1 << j)):

				p *= a[j]

		# if set bits is odd, then add to
		# the number of multiples
		if (bitsoncount(counter) & 1):
			odd += (m // p)
		else:

			even += (m // p)

	return odd - even


# Driver Code
a = [2, 3, 5, 7]
m = 100
n = len(a)
print(count(a, m, n))
