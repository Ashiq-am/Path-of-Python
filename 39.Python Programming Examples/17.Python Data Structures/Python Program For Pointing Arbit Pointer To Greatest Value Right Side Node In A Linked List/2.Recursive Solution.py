# Python3 program to point arbit pointers
# to highest value on its right

''' Link list node '''


# Node class
class newNode:

    # Constructor to initialize the
    # node object
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arbit = None


# This function populates arbit pointer
# in every node to the greatest value
# to its right.
maxNode = newNode(None)


def populateArbit(head):
    # using static maxNode to keep track
    # of maximum orbit node address on
    # right side
    global maxNode

    # if head is null simply return the list
    if (head == None):
        return

    ''' if head.next is null it means we
        reached at the last node just update
        the max and maxNode '''
    if (head.next == None):
        maxNode = head
        return

    ''' Calling the populateArbit to the
        next node '''
    populateArbit(head.next)

    ''' updating the arbit node of the
        current node with the maximum
        value on the right side '''
    head.arbit = maxNode

    ''' if current Node value id greater
        then the previous right node then
        update it '''
    if (head.data > maxNode.data and
            maxNode.data != None):
        maxNode = head
    return


# Utility function to prresult
# linked list
def printNextArbitPointers(node):
    print("Node ",
          "Next Pointer ",
          "Arbit Pointer")
    while (node != None):
        print(node.data,
              "	 ",
              end="")
        if (node.next):
            print(node.next.data,
                  "	 ",
                  end="")
        else:
            print("NULL", "	 ",
                  end="")
        if (node.arbit):
            print(node.arbit.data, end="")
        else:
            print("NULL", end="")
        print()
        node = node.next


# Driver code
head = newNode(5)
head.next = newNode(10)
head.next.next = newNode(2)
head.next.next.next = newNode(3)
populateArbit(head)
print("Resultant Linked List is:")
printNextArbitPointers(head)
