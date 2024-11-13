# Create Node class
class Node:
    def __init__(self, data=None):
        self.data = data
        # reference to next node in DLL
        self.next = None
        # reference to previous node in DLL
        self.prev = None
