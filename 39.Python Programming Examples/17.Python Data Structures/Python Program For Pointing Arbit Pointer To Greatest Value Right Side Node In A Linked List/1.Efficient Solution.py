# Python Program to point arbit pointers
# to highest value on its right

# Node class
class Node:

    # Constructor to initialize the
    # node object
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arbit = None


# Function to reverse the linked list
def reverse(head):
    prev = None
    current = head
    next = None

    while (current != None):
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


# This function populates arbit pointer
# in every node to the greatest value
# to its right.
def populateArbit(head):
    # Reverse given linked list
    head = reverse(head)

    # Initialize pointer to maximum
    # value node
    max = head

    # Traverse the reversed list
    temp = head.next
    while (temp != None):

        # Connect max through arbit
        # pointer
        temp.arbit = max

        # Update max if required
        if (max.data < temp.data):
            max = temp

        # Move ahead in reversed list
        temp = temp.next

    # Reverse modified linked list and
    # return head.
    return reverse(head)


# Utility function to print result
# linked list
def printNextArbitPointers(node):
    print("Node ",
          "Next Pointer ",
          "Arbit Pointer")
    while (node != None):

        print(node.data,
              "	 ",
              end="")

        if (node.next != None):
            print(node.next.data,
                  "	 ", end="")
        else:
            print("None",
                  "	 ", end="")

        if (node.arbit != None):
            print(node.arbit.data, end="")
        else:
            print("None", end="")

        print("")
        node = node.next


# Function to create a new node
# with given data
def newNode(data):
    new_node = Node(0)
    new_node.data = data
    new_node.next = None
    return new_node


# Driver code
head = newNode(5)
head.next = newNode(10)
head.next.next = newNode(2)
head.next.next.next = newNode(3)
head = populateArbit(head)

print("Resultant Linked List is: ")
printNextArbitPointers(head)
