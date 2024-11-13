class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_lca(root, node1, node2):
    if root is None:
        return None

    # If the root is one of the nodes, it is the LCA
    if root.value == node1 or root.value == node2:
        return root

    # Recursively find LCA in left and right subtrees
    left_lca = find_lca(root.left, node1, node2)
    right_lca = find_lca(root.right, node1, node2)

    # If both nodes are found in different subtrees, root is the LCA
    if left_lca and right_lca:
        return root

    # Otherwise, return the non-empty subtree
    return left_lca if left_lca else right_lca

# Example usage:
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Find LCA of nodes 4 and 5
node1_value = 4
node2_value = 5
lca_node = find_lca(root, node1_value, node2_value)
if lca_node:
    print(f"LCA of nodes {node1_value} and {node2_value} is: {lca_node.value}")
else:
    print(f"Nodes {node1_value} and {node2_value} are not found in the tree or they don't have a common ancestor.")
