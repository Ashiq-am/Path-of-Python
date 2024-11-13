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
    return query(node.left, left, mid, query_left, query_right) + query(node.right, mid + 1, right, query_left,
                                                                        query_right)
