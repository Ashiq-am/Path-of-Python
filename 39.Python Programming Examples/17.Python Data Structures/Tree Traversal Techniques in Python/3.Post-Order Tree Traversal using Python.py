class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None


# Preorder Traversal
def printPostOrder(node):
    if node is None:
        return

    # Traverse left subtree
    printPostOrder(node.left)

    # Traverse right subtree
    printPostOrder(node.right)

    # Visit Node
    print(node.data, end=" ")


# Driver code
if __name__ == "__main__":
    # Build the tree
    root = Node(10)
    root.left = Node(2)
    root.right = Node(20)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(15)
    root.right.right = Node(30)

    # Function call
    print("Postorder Traversal: ", end="")
    printPostOrder(root)
