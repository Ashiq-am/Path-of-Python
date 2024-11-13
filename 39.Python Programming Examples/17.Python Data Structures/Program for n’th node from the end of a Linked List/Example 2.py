def printNthFromLast(head, n):
    i = 0
    if (head == None):
        return
    printNthFromLast(head.next, n)
    i += 1
    if (i == n):
        print(head.data)

# This code is contributed by sunils0ni.
