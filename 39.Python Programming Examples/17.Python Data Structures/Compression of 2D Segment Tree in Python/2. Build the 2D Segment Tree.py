def build_segment_tree(matrix, start_row, end_row, start_col, end_col):
    if start_row == end_row and start_col == end_col:
        return SegmentTreeNode(matrix[start_row][start_col], start_row, end_row, start_col, end_col)

    mid_row = (start_row + end_row) // 2
    mid_col = (start_col + end_col) // 2

    node = SegmentTreeNode(0, start_row, end_row, start_col, end_col)
    node.left = build_segment_tree(matrix, start_row, mid_row, start_col, mid_col)
    node.right = build_segment_tree(matrix, start_row, mid_row, mid_col + 1, end_col)
    node.value = node.left.value + node.right.value

    return node
