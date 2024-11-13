# Python3 implementation to insert a
# node after the nth node from the end

# Structure of a node
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Function to get a new node
def getNode(data):
    # Allocate memory for the node
    newNode = Node(data)
    return newNode


# Function to insert a node after the
# nth node from the end
def insertAfterNthNode(head, n, x):
    # If list is empty
    if (head == None):
        return

    # Get a new node for the value 'x'
    newNode = getNode(x)

    # Initializing the slow and fast pointers
    slow_ptr = head
    fast_ptr = head

    # Move 'fast_ptr' to point to the nth
    # node from the beginning
    for i in range(1, n):
        fast_ptr = fast_ptr.next

    # Iterate until 'fast_ptr' points to the
    # last node
    while (fast_ptr.next != None):
        # Move both the pointers to the
        # respective next nodes
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next

    # Insert the 'newNode' by making the
    # necessary adjustment in the links
    newNode.next = slow_ptr.next
    slow_ptr.next = newNode


# Function to print the list
def printList(head):
    while (head != None):
        print(head.data, end=' ')
        head = head.next


# Driver code
if __name__ == '__main__':
    # Creating list 1.3.4.5
    head = getNode(1)
    head.next = getNode(3)
    head.next.next = getNode(4)
    head.next.next.next = getNode(5)

    n = 4
    x = 2

    print("Original Linked List: ", end='')
    printList(head)

    insertAfterNthNode(head, n, x)

    print("Linked List After Insertion: ", end = '')
    printList(head)

    # This code is contributed by rutvik_56
