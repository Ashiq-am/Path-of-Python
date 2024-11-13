class SegmentTreeNode:
    def __init__(self, value, start_row, end_row, start_col, end_col):
        self.value = value
        self.start_row = start_row
        self.end_row = end_row
        self.start_col = start_col
        self.end_col = end_col
        self.left = None
        self.right = None
