# Python3 implementation to find the sum of
# last 'n' nodes of the Linked List

# Linked List node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None
n = 0
sum = 0


# Function to insert a node at the
# beginning of the linked list
def push(head_ref, new_data):
    global head

    # Allocate node
    new_node = Node(0)

    # Put in the data
    new_node.data = new_data

    # Link the old list to the new node
    new_node.next = head_ref

    # Move the head to point to the
    # new node
    head_ref = new_node
    head = head_ref


# Utility function to find the sum of
# last 'n' nodes
def sumOfLastN_NodesUtil(head, n):
    global sum

    # if n == 0
    if (n <= 0):
        return 0

    st = []
    sum = 0

    # Traverses the list from left to right
    while (head != None):
        # Push the node's data onto the
        # stack 'st'
        st.append(head.data)

        # Move to next node
        head = head.next

    # Pop 'n' nodes from 'st' and
    # add them
    while (n):
        n -= 1
        sum += st[0]
        st.pop(0)

    # Required sum
    return sum


# Driver Code
head = None

# Create linked list 10.6.8.4.12
push(head, 12)
push(head, 4)
push(head, 8)
push(head, 6)
push(head, 10)

n = 2
print("Sum of last", n,
      "nodes =",
      sumOfLastN_NodesUtil(head, n))
# This code is contributed by shubhamsingh10
