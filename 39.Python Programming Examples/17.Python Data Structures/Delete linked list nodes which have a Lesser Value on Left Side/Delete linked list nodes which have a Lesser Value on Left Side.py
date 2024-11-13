# Python implementation of above approach
import math


# Structure of a linked list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to Delete nodes which have
# greater value node(s) on right side
def delNodes(head):
    current = head

    # Initialize max
    maxnode = head
    temp = None

    while (current != None and current.next != None):

        # If current is greater than max,
        # then update max and move current
        if (current.next.data <= maxnode.data):
            current = current.next
            maxnode = current

        # If current is smaller than max,
        # then delete current
        else:
            temp = current.next
            current.next = temp.next
        # free(temp)


# Utility function to insert a node at the beginning
def push(head_ref, new_data):
    new_node = Node(new_data)
    new_node.data = new_data
    new_node.next = head_ref
    head_ref = new_node
    return head_ref


# Utility function to print a linked list
def printList(head):
    while (head != None):
        print(head.data, end=" ")
        head = head.next
    print()


# Driver Code
if __name__ == '__main__':
    head = None

    # Create following linked list
    # 12.15.10.11.5.6.2.3
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 6)
    head = push(head, 5)
    head = push(head, 11)
    head = push(head, 10)
    head = push(head, 15)
    head = push(head, 12)

    print("Given Linked List: ", end="")
    printList(head)

    delNodes(head)

    print("\nModified Linked List: ", end="")
    printList(head)

# This code is contributed by AbhiThakur
