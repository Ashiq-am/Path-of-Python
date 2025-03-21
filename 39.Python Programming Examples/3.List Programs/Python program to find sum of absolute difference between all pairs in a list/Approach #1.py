# Python3 program to find sum of
# absolute differences in all pairs

def sumPairs(lst):
    diffs = []
    for i, x in enumerate(lst):
        for j, y in enumerate(lst):
            if i != j:
                diffs.append(abs(x - y))

    return int(sum(diffs) / 2)


# Driver program
lst = [1, 2, 3, 4]
print(sumPairs(lst))
