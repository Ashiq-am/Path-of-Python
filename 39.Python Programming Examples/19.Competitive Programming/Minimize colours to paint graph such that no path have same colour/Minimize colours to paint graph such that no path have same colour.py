# python code for the above approach:

# Function to find
# minimum number of colours required
def minColour(N, M, mat):

	# Create an adjacency list
	adj = [[] for _ in range(N + 1)]

	# Create indeg to store
	# indegree of every minion
	indeg = [0 for _ in range(N + 1)]

	for i in range(0, M):

		# Store mat[i][1] in adj[(mat[i][0])]
		# as mat[i][1] directs to mat[1][0]
		adj[(mat[i][0])].append(mat[i][1])
		indeg[(mat[i][1])] += 1

	# Initialize a variable lvl to store min
	# different colors required
	lvl = 0
	q = []

	for i in range(1, N + 1):
		if (indeg[i] == 0):
			q.append(i)

	if (len(q) == 0):
		return 0

	# Loop to use Topological sorting
	while (len(q) != 0):
		size = len(q)
		for k in range(0, size):
			e = q[0]
			q.pop(0)

			for it in adj[e]:
				indeg[it] -= 1
				if (indeg[it] == 0):
					q.append(it)

		lvl += 1

	# Return the minimum number of colours
	return lvl

# Driver code
if __name__ == "__main__":

	N = 5
	M = 6
	mat = [[1, 3], [2, 3], [3, 4], [1, 4], [2, 5], [3, 5]]

	# Function Call
	print(minColour(N, M, mat))

# This code is contributed by rakeshsahni
