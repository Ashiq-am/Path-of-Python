class SegmentTreeNode:
    def __init__(self, value, start_row, end_row, start_col, end_col):
        """
        Initialize a Segment Tree Node.

        Args:
            value (int): The value of the segment represented by this node.
            start_row (int): The starting row index of the segment.
            end_row (int): The ending row index of the segment.
            start_col (int): The starting column index of the segment.
            end_col (int): The ending column index of the segment.
        """
        self.value = value
        self.start_row = start_row
        self.end_row = end_row
        self.start_col = start_col
        self.end_col = end_col
        self.children = []

def build_segment_tree(matrix, start_row, end_row, start_col, end_col):
    """
    Recursively build a Segment Tree for a 2D matrix.

    Args:
        matrix (list): The 2D matrix to build the segment tree for.
        start_row (int): The starting row index of the current segment.
        end_row (int): The ending row index of the current segment.
        start_col (int): The starting column index of the current segment.
        end_col (int): The ending column index of the current segment.

    Returns:
        SegmentTreeNode: The root node of the constructed segment tree.
    """
    if start_row == end_row and start_col == end_col:
        return SegmentTreeNode(matrix[start_row][start_col], start_row, end_row, start_col, end_col)

    node = SegmentTreeNode(0, start_row, end_row, start_col, end_col)
    mid_row = (start_row + end_row) // 2
    mid_col = (start_col + end_col) // 2

    if start_row != end_row:
        if start_col != end_col:
            node.children.append(build_segment_tree(matrix, start_row, mid_row, start_col, mid_col))
            node.children.append(build_segment_tree(matrix, start_row, mid_row, mid_col + 1, end_col))
            node.children.append(build_segment_tree(matrix, mid_row + 1, end_row, start_col, mid_col))
            node.children.append(build_segment_tree(matrix, mid_row + 1, end_row, mid_col + 1, end_col))
        else:
            node.children.append(build_segment_tree(matrix, start_row, mid_row, start_col, end_col))
            node.children.append(build_segment_tree(matrix, mid_row + 1, end_row, start_col, end_col))
    else:
        node.children.append(build_segment_tree(matrix, start_row, end_row, start_col, mid_col))
        node.children.append(build_segment_tree(matrix, start_row, end_row, mid_col + 1, end_col))

    node.value = sum(child.value for child in node.children)
    return node

def compress_segment_tree(node):
    """
    Recursively compress a Segment Tree by removing redundant nodes.

    Args:
        node (SegmentTreeNode): The root node of the segment tree to compress.
    """
    if not node.children:
        return

    for child in node.children:
        compress_segment_tree(child)

    if all(child.value == node.children[0].value for child in node.children):
        node.value = node.children[0].value
        node.children = []

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

root = build_segment_tree(matrix, 0, len(matrix) - 1, 0, len(matrix[0]) - 1)
compress_segment_tree(root)

def print_tree(node, level=0):
    """
    Print the structure of the segment tree.

    Args:
        node (SegmentTreeNode): The root node of the segment tree.
        level (int): The level of the current node in the tree.
    """
    print(' ' * level * 4, node.value, (node.start_row, node.end_row), (node.start_col, node.end_col))
    for child in node.children:
        print_tree(child, level + 1)

print_tree(root)
