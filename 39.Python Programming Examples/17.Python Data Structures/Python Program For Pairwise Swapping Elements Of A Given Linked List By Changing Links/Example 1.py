# Python3 program to swap elements of
# linked list by changing links

# Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create and Handle list
# operations
class LinkedList:

    def __init__(self):

        # Head of list
        self.head = None

    # Add data to list
    def addToList(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        last = self.head

        while last.next:
            last = last.next

        last.next = newNode

    # Function to print nodes
    # in a given linked list
    def __str__(self):
        linkedListStr = ""
        temp = self.head

        while temp:
            linkedListStr = (linkedListStr +
                             str(temp.data) + " ")
            temp = temp.next

        return linkedListStr

    # Function to pairwise swap elements
    # of a linked list. It returns head of
    # the modified list, so return value
    # of this node must be assigned
    def pairWiseSwap(self):

        # If list is empty or with one
        # node
        if (self.head is None or
                self.head.next is None):
            return

        # Initialize previous and current
        # pointers
        prevNode = self.head
        currNode = self.head.next

        # Change head node
        self.head = currNode

        # Traverse the list
        while True:
            nextNode = currNode.next

            # Change next of current
            # node to previous node
            currNode.next = prevNode

            # If next node is the last node
            if nextNode.next is None:
                prevNode.next = nextNode
                break

            # Change next of previous to
            # next of next
            prevNode.next = nextNode.next

            # Update previous and current nodes
            prevNode = nextNode
            currNode = prevNode.next


# Driver Code
linkedList = LinkedList()
linkedList.addToList(1)
linkedList.addToList(2)
linkedList.addToList(3)
linkedList.addToList(4)
linkedList.addToList(5)
linkedList.addToList(6)
linkedList.addToList(7)

print("Linked list before calling"
      "pairwiseSwap() ", linkedList)

linkedList.pairWiseSwap()

print("Linked list after calling "
      "pairwiseSwap() ", linkedList)
# This code is contributed by AmiyaRanjanRout
