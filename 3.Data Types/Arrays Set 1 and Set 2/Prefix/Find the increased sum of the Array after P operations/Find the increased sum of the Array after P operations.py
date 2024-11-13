def findIncreasedSum(A, N, P):
	'''
		Created prefix and suffix arrays
		and initalise with -1 If prefix[i]
		is -1 then it means there is no
		postive element for the current
		element to its left Same holds
		for suffix array as well. Else
		prefix[i] or suffix[i] will
		represent the position of left
		positive and postive element
		for the current element
		respectively.
	'''
	prefix = [-1]*N
	suffix = [-1]*N

	# Initialing ans to zero.
	ans = 0

	# Building the prefix array
	for i in range(1, N):
		if(A[i - 1] > 0):
			prefix[i] = i - 1
		else:
			prefix[i] = prefix[i-1]

	# Building the suffix array
	for i in range(N-2, -1, -1):
		if(A[i + 1] > 0):
			suffix[i] = i + 1
		else:
			suffix[i] = suffix[i + 1]

	for i in range(N):

		# If the present is Zero.
		if A[i] == 0:

			# Checking if there is
			# left neighbour
			if i > 0:

				# Checking if there is
				# left positive element
				# exists or not
				if prefix[i] != -1:
					ans += 2*(max(0, P - i + prefix[i] + 1))

			# Checking if there is
			# right neighbour
			if i < N:

				# Checking if there is
				# right positive element
				# exists or not
				if suffix[i] != -1:
					ans += 2*(max(P - suffix[i] + i + 1, 0))
		else:

			# Checking if there is
			# left neighbour
			if i > 0:

				# Checking if there is
				# left element is non-zero
				# or not
				if A[i-1] > 0:
					ans += 2 * P
				else:
					ans += 2*(P-1)

			# Checking if there is
			# right neighbour
			if i < N-1:

				# Checking if there is
				# right element is
				# non-zero or not
				if A[i + 1] > 0:
					ans += 2 * P
				else:
					ans += 2*(P-1)
	return ans


N, P = 5, 2
A = [0, 5, 0, 4, 0]

# Funtion call
print(findIncreasedSum(A, N, P))
