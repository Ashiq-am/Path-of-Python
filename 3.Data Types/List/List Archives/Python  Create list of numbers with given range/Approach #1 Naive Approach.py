# Python3 Program to Create list
# with integers within given range

def createList(r1, r2):
    # Testing if range r1 and r2
    # are equal
    if (r1 == r2):
        return r1

    else:

        # Create empty list
        res = []

        # loop to append successors to
        # list until r2 is reached.
        while (r1 < r2 + 1):
            res.append(r1)
            r1 += 1
        return res

    # Driver Code


r1, r2 = -1, 1
print(createList(r1, r2))
