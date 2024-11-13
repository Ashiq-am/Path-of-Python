def recursive_function(n):
	if n > 10**6: # Adding a base case to terminate recursion
		return 0
	return n + recursive_function(n + 1)

recursive_function(1)
