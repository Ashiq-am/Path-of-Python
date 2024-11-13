# Python3 code to remove key element to
# end of linked list

# A Linked list Node
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# A utility function to create a new node.
def newNode(x):
    temp = Node(x)
    return temp


# Function to remove key to end
def keyToEnd(head, key):
    # Node to keep pointing to tail
    tail = head

    if (head == None):
        return None

    while (tail.next != None):
        tail = tail.next

    # Node to point to last of linked list
    last = tail
    current = head
    prev = None

    # Node prev2 to point to previous
    # when head.data!=key
    prev2 = None

    # Loop to perform operations to
    # remove key to end
    while (current != tail):
        if (current.data == key and prev2 == None):
            prev = current
            current = current.next
            head = current
            last.next = prev
            last = last.next
            last.next = None
            prev = None

        else:
            if (current.data == key and prev2 != None):
                prev = current
                current = current.next
                prev2.next = current
                last.next = prev
                last = last.next
                last.next = None

            elif (current != tail):
                prev2 = current
                current = current.next

    return head


# Function to display linked list
def printList(head):
    temp = head

    while (temp != None):
        print(temp.data, end=' ')
        temp = temp.next

    print()


# Driver Code
if __name__ == '__main__':
    root = newNode(5)
    root.next = newNode(2)
    root.next.next = newNode(2)
    root.next.next.next = newNode(7)
    root.next.next.next.next = newNode(2)
    root.next.next.next.next.next = newNode(2)
    root.next.next.next.next.next.next = newNode(2)

    key = 2
    print("Linked List before operations :")
    printList(root)
    print("Linked List after operations :")
    root = keyToEnd(root, key)

    printList(root)

# This code is contributed by rutvik_56
