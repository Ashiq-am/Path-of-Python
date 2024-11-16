# Python code to implement the approach

# Function to find maximum coins collected
# from the tree such that path sum from the
# root node to any leaf node is non zero


def max_coins_collect(N, edges, A):
	# Declaring Adjacency List for tree
	adj = [[] for _ in range(N)]

	# Filling Adjacency List
	for edge in edges:
		adj[edge[0]].append(edge[1])
		adj[edge[1]].append(edge[0])

	# DP array initialized with zero
	dp = [0] * N

	# dfs function
	def dfs(v, p):
		# iterating over child nodes
		for u in adj[v]:
			# if child of v is not equal to its parent
			if u != p:
				# call dfs function for child u
				dfs(u, v)
				# adding maximum coins chosen for child nodes
				dp[v] += dp[u]

		# base case
		if v != 0 and len(adj[v]) == 1:
			dp[v] = A[v]
		else:
			# Either choose maximum coins by child nodes or
			# coins present on the root of the tree
			dp[v] = min(dp[v], A[v])

	# calling dfs function
	dfs(0, -1)

	# variable to store total coins
	total_coins = sum(A)

	# returning final answer total_coins - minimum
	# coins required so that path sum from root to
	# any leaf node is non zero
	return total_coins - dp[0]


# Driver Code
if __name__ == "__main__":
	# Input
	N = 6
	A = [5, 2, 5, 2, 1, 1]
	edges = [
		[0, 1], [0, 2], [0, 3], [2, 4], [4, 5]
	]

	# Function Call
	print(max_coins_collect(N, edges, A))
