def appendNew(appendTo=None):
    if appendTo == None:
        appendTo = []
    appendTo.append(1)
    return appendTo


# Driver's code
print(appendNew())
print(appendNew())
