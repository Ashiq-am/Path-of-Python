class Node:
    def __init__(self, value=0, left=None, right=None):

        # Initialize a new node
        self.value = value  # The value stored in this node
        self.left = left    # Reference to the left child node
        self.right = right  # Reference to the right child node


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


def query(node, left, right, query_left, query_right):

    # Function to perform a range query on the segment tree
    if query_left > right or query_right < left:
        # If the query range does not overlap with the current segment, return 0
        return 0

    if query_left <= left and right <= query_right:

        # If the current segment is completely within the query range, return the value of the current node
        return node.value

    # Calculate the mid-point of the current segment
    mid = (left + right) // 2

    # Recursively query the left and right subtrees and return the sum of results
    return query(node.left, left, mid, query_left, query_right) + query(node.right, mid + 1, right, query_left, query_right)


# Example usage
if __name__ == "__main__":

    # Initial array
    arr = [1, 2, 3, 4, 5]

    # Build the initial segment tree
    root = build(arr, 0, len(arr) - 1)

    # Create a new version with an update (change the value at index 2 to 10)
    new_root = update(root, 0, len(arr) - 1, 2, 10)

    # Query the original and new versions
    print(query(root, 0, len(arr) - 1, 1, 3))      # Output: 9 (2+3+4)
    print(query(new_root, 0, len(arr) - 1, 1, 3))  # Output: 16 (2+10+4)
