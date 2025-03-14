# Recursive Python program to
# search an element in linked list

# Node class
class Node:

    # Function to initialize
    # the node object
    def __init__(self, data):
        # Assign data
        self.data = data

        # Initialize next as null
        self.next = None


class LinkedList:

    def __init__(self):

        # Initialize head as None
        self.head = None

    # This function insert a new node at
    # the beginning of the linked list
    def push(self, new_data):

        # Create a new Node
        new_node = Node(new_data)

        # Make next of new Node as head
        new_node.next = self.head

        # Move the head to
        # point to new Node
        self.head = new_node

    # Checks whether the value key
    # is present in linked list
    def search(self, li, key):

        # Base case
        if (not li):
            return False

        # If key is present in
        # current node, return true
        if (li.data == key):
            return True

        # Recur for remaining list
        return self.search(li.next, key)


# Driver Code
if __name__ == '__main__':

    li = LinkedList()

    li.push(1)
    li.push(2)
    li.push(3)
    li.push(4)

    key = 4

    if li.search(li.head, key):
        print("Yes")
    else:
        print("No")
# This code is contributed by Manoj Sharma
