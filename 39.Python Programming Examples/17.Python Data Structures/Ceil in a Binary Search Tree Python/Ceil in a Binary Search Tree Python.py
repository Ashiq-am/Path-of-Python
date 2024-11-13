class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findCeiling(root, value):
    if root is None:
        return None

    if root.value == value:
        return root.value

    if root.value < value:
        return findCeiling(root.right, value)

    ceil = findCeiling(root.left, value)
    return ceil if ceil is not None and ceil >= value else root.value

# Create the Binary Search Tree
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right = Node(14)
root.right.right.left = Node(13)

# Find the ceiling of 5
ceiling = findCeiling(root, 5)
print("Ceiling of 5:", ceiling)
