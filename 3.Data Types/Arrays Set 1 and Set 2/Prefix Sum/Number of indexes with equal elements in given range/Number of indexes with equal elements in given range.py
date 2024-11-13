# Python 3 program to count the
# number of indexes in range L R
# such that Ai = Ai + 1

# function that answers every
# query in O(r-l)
def answer_query(a, n, l, r):

	# traverse from l to r and
	# count the required indexes
	count = 0
	for i in range(l, r):
		if (a[i] == a[i + 1]):
			count += 1

	return count

# Driver Code
a = [1, 2, 2, 2, 3, 3, 4, 4, 4]
n = len(a)

# 1-st query
L = 1
R = 8
print(answer_query(a, n, L, R))

# 2nd query
L = 0
R = 4
print(answer_query(a, n, L, R)) 
