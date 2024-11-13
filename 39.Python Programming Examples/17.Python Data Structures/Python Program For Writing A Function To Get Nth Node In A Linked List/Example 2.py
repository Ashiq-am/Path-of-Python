# Python3 program to find n'th node in
# linked list using recursion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Given a reference (pointer to pointer) to
    # the head of a list and an int, push a new
    # node on the front of the list.

    # Make new node and add
    # into LinkedList
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def getNth(self, llist, position):

        # Call recursive method
        llist.getNthNode(self.head,
                         position, llist)

    # Recursive method to find Nth Node
    def getNthNode(self, head, position, llist):

        # Initialize count
        count = 0
        if (head):

            # If count is equal to position,
            # it means we have found the position
            if count == position:

                print(head.data)
            else:
                llist.getNthNode(head.next,
                                 position - 1, llist)
        else:
            # If head doesn't exist we have
            # traversed the LinkedList
            print('Index Doesn\'t exist')


# Driver Code
if __name__ == "__main__":
    llist = LinkedList()
    llist.push(1)
    llist.push(4)
    llist.push(1)
    llist.push(12)
    llist.push(1)

    # llist.getNth(llist,int(input()))
    # Enter the node position here
    # First argument is instance of LinkedList

    print("Element at Index 3 is", end=" ")
    llist.getNth(llist, 3)
# This code is contributed by Yogesh Joshi
