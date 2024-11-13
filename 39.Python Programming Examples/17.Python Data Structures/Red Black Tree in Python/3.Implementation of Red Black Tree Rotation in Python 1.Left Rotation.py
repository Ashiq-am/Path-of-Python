# function for left rotation of RB Tree
def rotate_left(self, node):
    right_child = node.right
    node.right = right_child.left

    if right_child.left is not None:
        right_child.left.parent = node

    right_child.parent = node.parent

    if node.parent is None:
        self.root = right_child
    elif node == node.parent.left:
        node.parent.left = right_child
    else:
        node.parent.right = right_child

    right_child.left = node
    node.parent = right_child
