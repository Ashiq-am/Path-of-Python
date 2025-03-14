"""
A Python3 program to swap kth node from
the beginning with kth node from the end
"""


class Node:
    def __init__(self, data,
                 next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, *args, **kwargs):
        self.head = Node(None)

    """
    Utility function to insert a node at
    the beginning
    @args:
        data: value of node
    """

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # Print linked list
    def printList(self):
        node = self.head

        while node.next is not None:
            print(node.data, end=" ")
            node = node.next

    # count number of node in linked list
    def countNodes(self):
        count = 0
        node = self.head
        while node.next is not None:
            count += 1
            node = node.next
        return count

    """
    Function for swapping kth nodes from
    both ends of linked list
    """

    def swapKth(self, k):

        # Count nodes in linked list
        n = self.countNodes()

        # Check if k is valid
        if n < k:
            return

        """
        If x (kth node from start) and
        y(kth node from end) are same
        """
        if (2 * k - 1) == n:
            return

        """
        Find the kth node from the beginning of
        the linked list. We also find previous
        of kth node because we need to update
        next pointer of the previous.
        """
        x = self.head
        x_prev = Node(None)
        for i in range(k - 1):
            x_prev = x
            x = x.next

        """
        Similarly, find the kth node from end
        and its previous. kth node from end
        is (n-k + 1)th node from beginning
        """
        y = self.head
        y_prev = Node(None)
        for i in range(n - k):
            y_prev = y
            y = y.next

        """
        If x_prev exists, then new next of it
        will be y. Consider the case when y->next
        is x, in this case, x_prev and y are same.
        So the statement "x_prev->next = y" creates
        a self loop. This self loop will be broken
        when we change y->next.
        """
        if x_prev is not None:
            x_prev.next = y

        # Same thing applies to y_prev
        if y_prev is not None:
            y_prev.next = x

        """
        Swap next pointers of x and y. These
        statements also break self loop if
        x->next is y or y->next is x
        """
        temp = x.next
        x.next = y.next
        y.next = temp

        # Change head pointers when k is 1 or n
        if k == 1:
            self.head = y

        if k == n:
            self.head = x


# Driver Code
llist = LinkedList()
for i in range(8, 0, -1):
    llist.push(i)
llist.printList()

for i in range(1, 9):
    llist.swapKth(i)
    print("Modified List for k = ", i)
    llist.printList()
    print("")
# This code is contributed by Pulkit
