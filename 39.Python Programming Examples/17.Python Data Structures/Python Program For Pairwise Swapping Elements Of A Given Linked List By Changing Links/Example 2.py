# Python3 program to pairwise swap
# linked list using recursive method

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

    # Function to print nodes in
    # a given linked list
    def __str__(self):
        linkedListStr = ""
        temp = self.head

        while temp:
            linkedListStr = (linkedListStr +
                             str(temp.data) + " ")
            temp = temp.next
        return linkedListStr

    # Function to pairwise swap elements of
    # a linked list. It returns head of the
    # modified list, so return value
    # of this node must be assigned
    def pairWiseSwap(self, node):

        # If list is empty or with one node
        if node is None or node.next is None:
            return node

        # Store head of list after
        # 2 nodes
        remaining = node.next.next

        # Change head
        newHead = node.next

        # Change next to second node
        node.next.next = node

        # Recur for remaining list and
        # change next of head
        node.next = self.pairWiseSwap(remaining)

        # Return new head of modified list
        return newHead


# Driver Code
linkedList = LinkedList()
linkedList.addToList(1)
linkedList.addToList(2)
linkedList.addToList(3)
linkedList.addToList(4)
linkedList.addToList(5)
linkedList.addToList(6)
linkedList.addToList(7)

print("Linked list before calling "
      "pairwiseSwap() ", linkedList)

linkedList.head = linkedList.pairWiseSwap(
    linkedList.head)
print("Linked list after calling "
      "pairwiseSwap() ", linkedList)
# This code is contributed by AmiyaRanjanRout
