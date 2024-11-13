# Python3 implementation to find the sum
# of last 'n' nodes of the Linked List
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


# Function to insert a node at the
# beginning of the linked list
def push(head_ref, new_data):
    # Allocate node
    new_node = Node(new_data)

    # Link the old list to the new node
    new_node.next = head_ref

    # Move the head to point to the
    # new node
    head_ref = new_node

    return head_ref


# Utility function to find the sum of
# last 'n' nodes
def sumOfLastN_NodesUtil(head, n):
    # if n == 0
    if (n <= 0):
        return 0

    sum = 0
    temp = 0
    ref_ptr = None
    main_ptr = None
    ref_ptr = main_ptr = head

    # Traverse 1st 'n' nodes through 'ref_ptr'
    # and accumulate all node's data to 'sum'
    while (ref_ptr != None and n):
        sum += ref_ptr.data

        # Move to next node
        ref_ptr = ref_ptr.next
        n -= 1

    # Traverse to the end of the linked list
    while (ref_ptr != None):
        # Accumulate all node's data to 'temp'
        # pointed by the 'main_ptr'
        temp += main_ptr.data

        # Accumulate all node's data to 'sum'
        # pointed by the 'ref_ptr'
        sum += ref_ptr.data

        # Move both the pointers to their
        # respective next nodes
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next

    # Required sum
    return (sum - temp)


# Driver code
if __name__ == '__main__':
    head = None

    # Create linked list 10.6.8.4.12
    head = push(head, 12)
    head = push(head, 4)
    head = push(head, 8)
    head = push(head, 6)
    head = push(head, 10)

    n = 2
    print("Sum of last ", n, " nodes = ",
          sumOfLastN_NodesUtil(head, n))
# This code is contributed by mohit kumar 29
