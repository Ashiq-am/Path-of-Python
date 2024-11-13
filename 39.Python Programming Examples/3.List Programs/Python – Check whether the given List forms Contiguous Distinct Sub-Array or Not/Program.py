from collections import Counter


# function to check contiguous
# distinct set arrray
def contig_distinct_setarr(l, n):
    c = Counter(l)
    a = list(set(l))

    b = []
    flag = True

    for j in c.values():

        # iterating and moving it to another
        # array if already present we print NO
        # when it finds no. of different elements
        # to be equal if no. of x's = no. of y's
        # So we break of the loop
        if j not in b:
            b.append(j)
        else:
            print("NO")
            flag = False
            break

    # If already there are similar elements
    # in c.values()- the count of elements
    # flag = False and we dont need to check
    # the below condition If not flag = False
    # then the iterate through the array loop
    if (flag != False):
        i, k = 0, 0

        # for each elements in set a
        # cou stores the count of a[i]
        while k < len(a):
            cou = c[a[i]]
            x = l.index(a[i])

            # here we extract thecontiguous
            # sub array of length equal to
            # the count of the element
            temp = (l[x:x + cou])

            # if the number of elements of
            # subsequences is not equal to
            # the value of element in the
            # dictionary print NO
            if len(temp) != c[a[i]]:
                print("NO")
                flag = False
                break

            k += 1
            i += 1

        # if we have iterated all over the array
        # and the condition is satisfied we print
        # YES
        if flag == True:
            print("YES")


# initialize the array and its length
n = 6
l = [1, 1, 3, 6, 6, 6]
contig_distinct_setarr(l, n)
