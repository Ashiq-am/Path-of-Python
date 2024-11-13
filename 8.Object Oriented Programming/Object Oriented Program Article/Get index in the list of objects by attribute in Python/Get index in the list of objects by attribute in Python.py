# This code gets the index in the
# list of objects by attribute.

class X:
    def __init__(self, val):
        self.val = val


def getIndex(li, target):
    for index, x in enumerate(li):
        if x.val == target:
            return index
    return -1


# Driver code
li = [1, 2, 3, 4, 5, 6]

# Converting all the items in
# list to object of class X
a = list()
for i in li:
    a.append(X(i))

print(getIndex(a, 3))
