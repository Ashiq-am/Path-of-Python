# Python3 program to merge two sorted linked
# lists without using any extra space and
# without changing links of first list

# Structure for a linked list node
class Node:
    def __init__(self):
        self.data = 0
        self.next = None


# Given a reference (pointer to pointer) to
# the head of a list and an int, push a new
# node on the front of the list.
def push(head_ref, new_data):
    # Allocate node
    new_node = Node()

    # Put in the data
    new_node.data = new_data

    # Link the old list off the
    # new node
    new_node.next = (head_ref)

    # Move the head to point to
    # the new node
    (head_ref) = new_node
    return head_ref


# Function to merge two sorted linked lists
# LL1 and LL2 without using any extra space.
def mergeLists(a, b):
    # Run till either one of a
    # or b runs out
    while (a and b):

        # For each element of LL1, compare
        # it with first element of LL2.
        if (a.data > b.data):

            # Swap the two elements involved
            # if LL1 has a greater element
            a.data, b.data = b.data, a.data

            temp = b

            # To keep LL2 sorted, place first
            # element of LL2 at its correct place
            if (b.next and b.data > b.next.data):
                b = b.next
                ptr = b
                prev = None

                # Find mismatch by traversing the
                # second linked list once
                while (ptr and ptr.data < temp.data):
                    prev = ptr
                    ptr = ptr.next

                # Correct the pointers
                prev.next = temp
                temp.next = ptr

        # Move LL1 pointer to next element
        a = a.next


# Function to print the linked link
def printList(head):
    while (head):
        print(head.data, end='->')
        head = head.next

    print('NULL')


# Driver code
if __name__ == '__main__':
    a = None
    a = push(a, 10)
    a = push(a, 8)
    a = push(a, 7)
    a = push(a, 4)
    a = push(a, 2)

    b = None
    b = push(b, 12)
    b = push(b, 3)
    b = push(b, 1)

    mergeLists(a, b)

    print("First List: ", end='')
    printList(a)

    print("Second List: ", end='')
    printList(b)
