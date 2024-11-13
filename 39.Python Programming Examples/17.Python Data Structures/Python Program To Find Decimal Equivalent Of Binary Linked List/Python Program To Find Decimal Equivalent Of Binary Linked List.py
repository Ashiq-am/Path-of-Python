# Python3 program to find decimal value
# of binary linked list

# Node Class
class Node:

    # Function to initialise the
    # node object
    def __init__(self, data):
        # Assign data
        self.data = data

        # Initialize next as null
        self.next = None


# Linked List class contains
# a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Returns decimal value of binary
    # linked list
    def decimalValue(self, head):
        # Initialized result
        res = 0

        # Traverse linked list
        while head:
            # Multiply result by 2 and
            # add head's data
            res = (res << 1) + head.data

            # Move Next
            head = head.next

        return res


# Driver code
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    llist.head.next = Node(0)
    llist.head.next.next = Node(1)
    llist.head.next.next.next = Node(1)
    print("Decimal Value is {}".format(llist.decimalValue(llist.head)))
# This code is contributed by Mohit Jangra
