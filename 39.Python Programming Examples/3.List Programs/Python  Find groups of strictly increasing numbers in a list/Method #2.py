# Python3 program to Find groups
# of strictly increasing numbers within

def groupSequence(l):
    start_bound = [i for i in range(len(l) - 1)
                   if (l == 0 or l[i] != l[i - 1] + 1)
                   and l[i + 1] == l[i] + 1]

    end_bound = [i for i in range(1, len(l))
                 if l[i] == l[i - 1] + 1 and
                 (i == len(l) - 1 or l[i + 1] != l[i] + 1)]

    return [l[start_bound[i]:end_bound[i] + 1]
            for i in range(len(start_bound))]


# Driver program
l = [8, 9, 10, 7, 8, 1, 2, 3]
print(list(groupSequence(l)))
