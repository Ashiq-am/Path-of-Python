# Python3 program to Find groups
# of strictly increasing numbers within

def groupSequence(lst):
    res = [[lst[0]]]

    for i in range(1, len(lst)):
        if lst[i - 1] + 1 == lst[i]:
            res[-1].append(lst[i])

        else:
            res.append([lst[i]])
    return res


# Driver program
l = [8, 9, 10, 7, 8, 1, 2, 3]
print(groupSequence(l))
