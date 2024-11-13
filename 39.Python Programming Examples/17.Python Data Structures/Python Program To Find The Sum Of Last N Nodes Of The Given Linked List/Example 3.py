# Python implementation to find the sum of last
# 'n' Nodes of the Linked List
''' A Linked list Node '''


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

    # Move the head to point the new Node
    head_ref = new_Node
    head = head_ref
    return head


def reverseList():
    global head
    current, prev, next = None,
    None, None
    current = head
    prev = None

    while (current != None):
        next = current.next
        current.next = prev
        prev = current
        current = next

    head = prev


# Utility function to find the sum
# of last 'n' Nodes
def sumOfLastN_NodesUtil(n):
    # if n == 0
    if (n <= 0):
        return 0

    # Reverse the linked list
    reverseList()

    sum = 0
    current = head

    # Traverse the 1st 'n' Nodes of the
    # reversed linked list and add them
    while (current != None and n > 0):
        # Accumulate Node's data to 'sum'
        sum += current.data

        # Move to next Node
        current = current.next
        n -= 1

    # Reverse back the linked list
    reverseList()

    # Required sum
    return sum


# Driver code
if __name__ == '__main__':
    # Create linked list 10.6.8.4.12
    head = push(head, 12)
    head = push(head, 4)
    head = push(head, 8)
    head = push(head, 6)
    head = push(head, 10)

    n = 2
    print("Sum of last ", n,
          " Nodes = ",
          sumOfLastN_NodesUtil(n))
# This code is contributed by Princi Singh
