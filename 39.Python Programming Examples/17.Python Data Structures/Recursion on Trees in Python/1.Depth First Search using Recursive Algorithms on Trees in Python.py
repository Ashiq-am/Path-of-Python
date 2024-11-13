class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs_recursive(node):
    if node is None:
        return

    # Visit the current node
    print(node.value)

    # Traverse left subtree
    dfs_recursive(node.left)

    # Traverse right subtree
    dfs_recursive(node.right)


# Example usage:
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Perform DFS recursively
print("Depth-First Search (DFS) Recursive:")
dfs_recursive(root)
