# Python3 program to print reverse
# of a linked list

# Node class
class Node:

    # Constructor to initialize
    # the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Recursive function to print
    # linked list in reverse order
    def printrev(self, temp):
        if temp:
            self.printrev(temp.next)
            print(temp.data, end=' ')
        else:
            return

    # Function to insert a new node
    # at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


# Driver code
llist = LinkedList()

llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

llist.printrev(llist.head)
