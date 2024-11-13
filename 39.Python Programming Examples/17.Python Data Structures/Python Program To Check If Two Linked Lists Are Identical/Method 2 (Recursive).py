# A recursive Python3 function to check
# if two linked lists are identical
# or not
def areIdentical(a, b):
    # If both lists are empty
    if (a == None and b == None):
        return True

    # If both lists are not empty,
    # then data of current nodes must
    # match, and same should be recursively
    # true for rest of the nodes.
    if (a != None and b != None):
        return ((a.data == b.data) and
                areIdentical(a.next, b.next))

    # If we reach here, then one of the lists
    # is empty and other is not
    return False
# This code is contributed by Princi Singh
