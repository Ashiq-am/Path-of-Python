# Declare variables for the number of nodes, the constant
# c, the farthest node p, the array of node values a, and
# the array of sums s
N = 2 * 10**5 + 7

# Read the number of nodes and the constant c
n, c = 4, 10

a = [0, 20, 15, 10]
s = [0] * N

p = 1

# Loop over each node
for i in range(1, n + 1):

	# Calculate the sum of the values up to the current node
	s[i] = s[i - 1] + a[i - 1]

	# If the sum of the values up to p +
	# the value of the current node is greater than or
	# equal to i*c, update p to i
	if s[p] + a[i - 1] >= i * c:
		p = i

# If p is equal to n, print "Yes". Otherwise, print "No"
print("Yes" if p == n else "No")

# This code is contributed by shivamgupta0987654321
