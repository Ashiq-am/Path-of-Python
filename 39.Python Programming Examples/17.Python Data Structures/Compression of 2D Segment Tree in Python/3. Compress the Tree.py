def compress_segment_tree(node):
    if node.left is None and node.right is None:
        return

    if node.left.value == node.right.value:
        node.value = node.left.value
        node.left = None
        node.right = None
    else:
        compress_segment_tree(node.left)
        compress_segment_tree(node.right)
