# Python program to rearrange linked list
# in place

# Node Class
class Node:

    # Constructor to create
    # a new node
    def __init__(self, d):
        self.data = d
        self.next = None


def printlist(node):
    if (node == None):
        return
    while (node != None):
        print(node.data, " -> ",
              end="")
        node = node.next


def reverselist(node):
    prev = None
    curr = node
    next = None
    while (curr != None):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    node = prev
    return node


def rearrange(node):
    # 1) Find the middle point using
    # tortoise and hare method
    slow = node
    fast = slow.next

    while (fast != None and
           fast.next != None):
        slow = slow.next
        fast = fast.next.next

    # 2) Split the linked list in
    # two halves
    # node1, head of first half
    # 1 -> 2 -> 3
    # node2, head of second half
    # 4 -> 5
    node1 = node
    node2 = slow.next
    slow.next = None

    # 3) Reverse the second half,
    # i.e., 5 -> 4
    node2 = reverselist(node2)

    # 4) Merge alternate nodes
    # Assign dummy Node
    node = Node(0)

    # curr is the pointer to this
    # dummy Node, which will be
    # used to form the new list
    curr = node

    while (node1 != None or
           node2 != None):

        # First add the element from
        # first list
        if (node1 != None):
            curr.next = node1
            curr = curr.next
            node1 = node1.next

        # Then add the element from
        # second list
        if (node2 != None):
            curr.next = node2
            curr = curr.next
            node2 = node2.next

    # Assign the head of the new list
    # to head pointer
    node = node.next


head = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Print original list
printlist(head)

# Rearrange list as per ques
rearrange(head)
print()

# Print modified list
printlist(head)
# This code is contributed by ab2127
