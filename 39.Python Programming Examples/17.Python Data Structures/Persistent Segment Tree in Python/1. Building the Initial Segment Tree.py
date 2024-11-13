def build(arr, left, right):

    # Function to build the initial segment tree
    if left == right:

        # If the current segment is a single element, create a leaf node
        return Node(value=arr[left])

    # Calculate the mid-point of the current segment
    mid = (left + right) // 2

    # Recursively build the left and right subtrees
    left_child = build(arr, left, mid)
    right_child = build(arr, mid + 1, right)

    # Create a new node with the sum of values of left and right children
    return Node(value=left_child.value + right_child.value, left=left_child, right=right_child)
