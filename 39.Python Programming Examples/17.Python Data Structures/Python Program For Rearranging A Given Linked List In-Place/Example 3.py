# Python3 program to implement
# the above approach
class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


left = None


# Function to print the list
def printlist(head):
    while (head != None):
        print(head.data, end=" ")
        if (head.next != None):
            print("->", end="")

        head = head.next

    print()


# Function to rearrange
def rearrange(head):
    global left
    if (head != None):
        left = head
        reorderListUtil(left)


def reorderListUtil(right):
    global left
    if (right == None):
        return

    reorderListUtil(right.next)

    # We set left = null, when we
    # reach stop condition, so no
    # processing required after that
    if (left == None):
        return

    # Stop condition: odd case :
    # left = right, even
    # case : left.next = right
    if (left != right and
            left.next != right):
        temp = left.next
        left.next = right
        right.next = temp
        left = temp
    else:

        # Stop condition , set null
        # to left nodes
        if (left.next == right):

            # Even case
            left.next.next = None
            left = None
        else:

            # Odd case
            left.next = None
            left = None


# Driver code
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Print original list
printlist(head)

# Modify the list
rearrange(head)

# Print modified list
printlist(head)
# This code is contributed by patel2127
