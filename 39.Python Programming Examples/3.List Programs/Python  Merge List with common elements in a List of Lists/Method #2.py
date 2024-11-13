#Python code to merge all sublist having common elements.

#Importing
from collections import defaultdict

#merge function to merge all sublist having common elements.
def merge_common(lists):
	neigh = defaultdict(set)
	visited = set()
	for each in lists:
		for item in each:
			neigh[item].update(each)
	def comp(node, neigh = neigh, visited = visited, vis = visited.add):
		nodes = set([node])
		next_node = nodes.pop
		while nodes:
			node = next_node()
			vis(node)
			nodes |= neigh[node] - visited
			yield node
	for node in neigh:
		if node not in visited:
			yield sorted(comp(node))

#Input list initialization
Input = [['z','x','y'], ['y','g','e'], ['z'],['x','p'],
		['a','b'], ['y','a'], ['d','g']]

#Calling merge function
Output = list(merge_common(Input))

#Printing function
print("Initial list of list is :")
print(Input)

print("List of list after merging is:")
print(Output)
