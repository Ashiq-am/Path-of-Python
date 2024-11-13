def flattenList2(head):
    headcop = head
    save = []
    save.append(head)
    prev = None

    while (len(save) != 0):
        temp = save[-1]
        save.pop()

        if (temp.next):
            save.append(temp.next)
        if (temp.down):
            save.append(temp.down)
        if (prev != None):
            prev.next = temp

        prev = temp

    return headcop
# This code is contributed by rutvik_56
