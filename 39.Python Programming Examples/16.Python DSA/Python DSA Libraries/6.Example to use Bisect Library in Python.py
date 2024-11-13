from treelib import Node, Tree

# Create a new binary tree
tree = Tree()

# Add nodes to the tree
tree.create_node("Root", "root") # Create the root node
# Create a left child node
tree.create_node("Left Child", "left", parent="root")
# Create a right child node
tree.create_node("Right Child", "right", parent="root")

# Add more nodes to the left child
# Create a left grandchild node
tree.create_node("Left Grandchild", "left_grand", parent="left")
# Create a right grandchild node
tree.create_node("Right Grandchild", "right_grand", parent="left")

# Print the tree structure
print("Tree structure:")
tree.show()

# Traverse the tree (pre-order traversal)
print("\nPre-order traversal:")
for node in tree.all_nodes():
	print(node.tag)

# Visualize the tree
tree.show(line_type="ascii-em")

# Visualize the tree using Graphviz (requires Graphviz installed)
# tree.show()
