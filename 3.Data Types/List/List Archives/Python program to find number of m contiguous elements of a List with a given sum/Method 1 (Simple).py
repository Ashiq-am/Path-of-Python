# Python program to find number of
# m contiguous elements of a list
# with sum s


def SearchWay(l, s, m):
    # initialise sum and
    # count to 0
    sum1 = 0
    count = 0

    # iterate from start of
    # list to end
    for i in range(len(l) - m + 1):

        # get sum f m elements
        # starting from index i
        for j in range(i, i + m):
            sum1 += l[j]

        # if the sum of elements equal
        # s increment count
        if sum1 == s:
            count += 1

        sum1 = 0

    return count


# Driver's code
l = [1, 2, 1, 3, 2]
s = 3
m = 2

ans = SearchWay(l, s, m)
print(ans)
