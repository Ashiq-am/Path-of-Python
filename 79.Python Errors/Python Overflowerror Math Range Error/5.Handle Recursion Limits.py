import sys

def recursive_function(n):
	if n <= 0:
		return
	print("Recursion level:", n)
	recursive_function(n - 1)

# Increase recursion limit
sys.setrecursionlimit(10000)

# Call the recursive function
recursive_function(5000)
