def update(prev_node, left, right, idx, new_value):

    # Function to perform an update operation on the segment tree persistently
    if left == right:

        # If the current segment is a single element, create a new node with the updated value
        return Node(value=new_value)

    # Calculate the mid-point of the current segment
    mid = (left + right) // 2

    # Determine whether the index to be updated lies in the left or right subtree
    if idx <= mid:

        # Recursively update the left subtree, keep the right subtree unchanged
        left_child = update(prev_node.left, left, mid, idx, new_value)
        right_child = prev_node.right
    else:

        # Recursively update the right subtree, keep the left subtree unchanged
        left_child = prev_node.left
        right_child = update(prev_node.right, mid + 1, right, idx, new_value)

    # Create a new node with the sum of values of the updated left and right children
    return Node(value=left_child.value + right_child.value, left=left_child, right=right_child)
