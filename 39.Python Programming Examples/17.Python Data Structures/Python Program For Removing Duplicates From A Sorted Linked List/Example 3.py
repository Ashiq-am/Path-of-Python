# Python3 program to remove duplicates
# from a sorted linked list
import math


# Link list node
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# The function removes duplicates
# from the given linked list
def removeDuplicates(head):
    # Do nothing if the list consist of
    # only one element or empty
    if (head == None and
            head.next == None):
        return

    # Construct a pointer
    # pointing towards head
    current = head

    # Initialise a while loop till the
    # second last node of the linkedlist
    while (current.next):

        # If the data of current and next
        # node is equal we will skip the
        # node between them
        if current.data == current.next.data:
            current.next = current.next.next

        # If the data of current and
        # next node is different move
        # the pointer to the next node
        else:
            current = current.next

    return


# UTILITY FUNCTIONS
# Function to insert a node at the
# beginning of the linked list
def push(head_ref, new_data):
    # Allocate node
    new_node = Node(new_data)

    # Put in the data
    new_node.data = new_data

    # Link the old list off
    # the new node
    new_node.next = head_ref

    # Move the head to point
    # to the new node
    head_ref = new_node

    return head_ref


# Function to print nodes
# in a given linked list
def printList(node):
    while (node != None):
        print(node.data, end=" ")
        node = node.next


# Driver code
if __name__ == '__main__':
    head = None
    head = push(head, 20)
    head = push(head, 13)
    head = push(head, 13)
    head = push(head, 11)
    head = push(head, 11)
    head = push(head, 11)

    print("List before removal of ""duplicates ", end="")
    printList(head)

    removeDuplicates(head)

    print("List after removal of ""elements ", end="")
    printList(head)
# This code is contributed by MukulTomar
