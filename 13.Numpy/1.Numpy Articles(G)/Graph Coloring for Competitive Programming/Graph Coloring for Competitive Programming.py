from typing import List

class GFG:
	def __init__(self):
		# Boolean variable to check if the graph is bi-partite or not
		self.ok = True

	# Function to check if the graph is bi-partite
	def is_bipartite(self, g: List[List[int]], color: List[int], vis: List[bool], node: int, paint: int):
		# If the current node is already painted and it doesn't
		# match the required paint, return false
		if color[node] != -1 and color[node] != paint:
			self.ok = False
			return

		# Color the node with the current paint
		color[node] = paint

		# If the node is already visited, return
		if vis[node]:
			return

		# Mark the node as visited
		vis[node] = True

		# Traverse each adjacent child node
		for child in g[node]:
			# Recursive call for each adjacent child with opposite paint
			self.is_bipartite(g, color, vis, child, paint ^ 1)

	# Main method to execute the code
	def main(self):
		# Create an instance of the GFG class (or you can create a
		# new instance and call the method)
		gfg = GFG()
