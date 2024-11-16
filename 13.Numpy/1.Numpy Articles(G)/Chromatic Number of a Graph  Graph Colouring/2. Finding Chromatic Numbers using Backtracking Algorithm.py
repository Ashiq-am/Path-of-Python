from typing import List, Set

def is_safe(v, graph, color, c):
	for neighbor in graph[v]:
		if color[neighbor] == c:
			return False # If any adjacent vertex has the same color, it's not safe
	return True

def graph_coloring_util(v, graph, color, m):
	if v == len(graph):
		return True # All vertices are colored, a solution is found

	for c in range(1, m + 1):
		if is_safe(v, graph, color, c):
			color[v] = c

			# Recur for the next vertices
			if graph_coloring_util(v + 1, graph, color, m):
				return True

			# Backtrack
			color[v] = 0

	return False # No solution found for this coloring

def graph_coloring(graph, m):
	n = len(graph)
	color = [0] * n

	if not graph_coloring_util(0, graph, color, m):
		print("No feasible solution exists")
		return 0

	# Print the solution
	print("Vertex colors:", end=" ")
	for c in color:
		print(c, end=" ")
	print()

	# Count unique colors to determine chromatic number
	unique_colors = set(color)
	return len(unique_colors)

if __name__ == "__main__":
	# Sample graph represented as an adjacency list
	graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]

	# Set the maximum number of colors
	max_colors = 3

	# Find and output the chromatic number
	chromatic_number = graph_coloring(graph, max_colors)
	print("Chromatic Number:", chromatic_number)
