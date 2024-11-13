# Python implementation to insert a node after
# the n-th node from the end

# Linked List node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# function to get a new node
def getNode(data):
    # allocate memory for the node
    newNode = Node(0)

    # put in the data
    newNode.data = data
    newNode.next = None
    return newNode


# function to insert a node after the
# nth node from the end
def insertAfterNthNode(head, n, x):
    # if list is empty
    if (head == None):
        return

    # get a new node for the value 'x'
    newNode = getNode(x)
    ptr = head
    len = 0
    i = 0

    # find length of the list, i.e, the
    # number of nodes in the list
    while (ptr != None):
        len = len + 1
        ptr = ptr.next

    # traverse up to the nth node from the end
    ptr = head
    i = 1
    while (i <= (len - n)):
        ptr = ptr.next
        i = i + 1

    # insert the 'newNode' by making the
    # necessary adjustment in the links
    newNode.next = ptr.next
    ptr.next = newNode


# function to print the list
def printList(head):
    while (head != None):
        print(head.data, end=" ")
        head = head.next


# Driver code

# Creating list 1->3->4->5
head = getNode(1)
head.next = getNode(3)
head.next.next = getNode(4)
head.next.next.next = getNode(5)

n = 4
x = 2

print("Original Linked List: ")
printList(head)

insertAfterNthNode(head, n, x)
print()
print("Linked List After Insertion: ")
printList(head)

# This code is contributed by Arnab Kundu
