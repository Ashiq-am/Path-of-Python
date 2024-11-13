# A node representing a Binomial Tree.
class Node:
    def __init__(self, key):
        # Initialize node data,
        # degree, and pointers.
        self.data = key
        self.degree = 0
        self.child = None
        self.parent = None
        self.sibling = None

# Merges two Binomial Trees.

def mergeBinomialTrees(b1, b2):
    # Ensure b1 has smaller value.
    if b1.data > b2.data:
        b1, b2 = b2, b1

    # Make b2 a child of b1.
    b2.parent = b1
    b2.sibling = b1.child
    b1.child = b2
    b1.degree += 1

    return b1

# Performs union operation on two binomial heaps.

def unionBionomialHeap(l1, l2):
    _new = []
    it = ot = 0

    # Merge sorted lists based on degree.
    while it < len(l1) and ot < len(l2):
        if l1[it].degree <= l2[ot].degree:
            _new.append(l1[it])
            it += 1
        else:
            _new.append(l2[ot])
            ot += 1

    # Append remaining elements from lists.
    while it < len(l1):
        _new.append(l1[it])
        it += 1

    while ot < len(l2):
        _new.append(l2[ot])
        ot += 1

    return _new

# Rearranges the heap to ensure increasing order
# of degree and no two trees have the same degree.

def adjust(_heap):
    if len(_heap) <= 1:
        return _heap

    new_heap = []
    it1 = it2 = it3 = 0

    if len(_heap) == 2:
        it2 = 1
        it3 = len(_heap)
    else:
        it2 = 1
        it3 = 2

    while it1 < len(_heap):
        if it2 == len(_heap):
            it1 += 1

        elif _heap[it1].degree < _heap[it2].degree:
            it1 += 1
            it2 += 1
            if it3 < len(_heap):
                it3 += 1

        elif it3 < len(_heap) and _heap[it1].degree == _heap[it2].degree == _heap[it3].degree:
            it1 += 1
            it2 += 1
            it3 += 1

        elif _heap[it1].degree == _heap[it2].degree:
            # Merge trees with same degree.
            _heap[it1] = mergeBinomialTrees(_heap[it1], _heap[it2])
            del _heap[it2]
            if it3 < len(_heap):
                it3 += 1

    return _heap

# Inserts a Binomial Tree into a binomial heap.


def insertATreeInHeap(_heap, tree):
    temp = [tree]
    temp = unionBionomialHeap(_heap, temp)
    return adjust(temp)

# Removes the minimum key element from the binomial heap
# and returns the binomial heap.

def removeMinFromTreeReturnBHeap(tree):
    heap = []
    temp = tree.child

    # Create a heap from the children of the minimum element.
    while temp:
        lo = temp
        temp = temp.sibling
        lo.sibling = None
        heap.insert(0, lo)

    return heap

# Inserts a key into the binomial heap.

def insert(_head, key):
    temp = Node(key)
    return insertATreeInHeap(_head, temp)

# Returns the pointer of the minimum value Node present
# in the binomial heap.

def getMin(_heap):
    temp = _heap[0]

    # Find the minimum element in the heap.
    for node in _heap:
        if node.data < temp.data:
            temp = node

    return temp

# Extracts the minimum element from the binomial heap.

def extractMin(_heap):
    new_heap = []
    lo = []

    # Get the minimum element.
    temp = getMin(_heap)

    # Remove the minimum element from the heap.
    for node in _heap:
        if node != temp:
            new_heap.append(node)

    # Merge heap with children of the minimum element.
    lo = removeMinFromTreeReturnBHeap(temp)
    new_heap = unionBionomialHeap(new_heap, lo)
    new_heap = adjust(new_heap)

    return new_heap

# Prints a Binomial Tree.

def printTree(h):
    while h:
        # Print current node's data.
        print(h.data, end=" ")
        # Recursively print child nodes.
        printTree(h.child)
        h = h.sibling

# Prints a binomial heap.

def printHeap(_heap):
    for node in _heap:
        # Print each Binomial Tree in the heap.
        printTree(node)

# Driver program to test the functions.
if __name__ == "__main__":
    _heap = []

    # Insert data into the heap.
    _heap = insert(_heap, 10)
    _heap = insert(_heap, 20)
    _heap = insert(_heap, 30)

    print("Heap elements after insertion:")
    # Print the heap after insertion.
    printHeap(_heap)

    # Find and print the minimum element.
    temp = getMin(_heap)
    print("\nMinimum element of heap:", temp.data)

    # Delete the minimum element from the heap.
    _heap = extractMin(_heap)
    print("Heap after deletion of minimum element:")
    # Print the heap after deletion.
    printHeap(_heap)
