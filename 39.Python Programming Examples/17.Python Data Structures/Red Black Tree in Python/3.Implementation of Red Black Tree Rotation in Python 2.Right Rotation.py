# function for right rotation of RB Tree
def rotate_right(self, node):
    left_child = node.left
    node.left = left_child.right

    if left_child.right is not None:
        left_child.right.parent = node

    left_child.parent = node.parent

    if node.parent is None:
        self.root = left_child
    elif node == node.parent.right:
        node.parent.right = left_child
    else:
        node.parent.left = left_child

    left_child.right = node
    node.parent = left_child
