# Python3 implementation to find the sum
# of last 'n' Nodes of the Linked List

# A Linked list Node
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


head = None


# Function to insert a Node at the
# beginning of the linked list
def push(head_ref, new_data):
    # Allocate Node
    new_Node = Node(new_data)

    # Put in the data
    new_Node.data = new_data

    # Link the old list to the new Node
    new_Node.next = head_ref

    # Move the head to point to the new Node
    head_ref = new_Node
    head = head_ref
    return head


# Utility function to find the sum of
# last 'n' Nodes
def sumOfLastN_NodesUtil(head, n):
    # If n == 0
    if (n <= 0):
        return 0

    sum = 0
    len = 0
    temp = head

    # Calculate the length of the
    # linked list
    while (temp != None):
        len += 1
        temp = temp.next

    # Count of first (len - n) Nodes
    c = len - n
    temp = head

    # Just traverse the 1st 'c' Nodes
    while (temp != None and c > 0):
        # Move to next Node
        temp = temp.next
        c -= 1

    # Now traverse the last 'n' Nodes
    # and add them
    while (temp != None):
        # Accumulate Node's data to sum
        sum += temp.data

        # Move to next Node
        temp = temp.next

    # Required sum
    return sum


# Driver code
if __name__ == '__main__':
    # Create linked list 10->6->8->4->12
    head = push(head, 12)
    head = push(head, 4)
    head = push(head, 8)
    head = push(head, 6)
    head = push(head, 10)

    n = 2

    print("Sum of last ", n, " Nodes = ",
          sumOfLastN_NodesUtil(head, n))

# This code is contributed by Princi Singh
