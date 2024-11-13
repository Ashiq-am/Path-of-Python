# Python program to find number of
# m contiguous elements of a list
# with sum s


def SearchWay(l, s, m):
    n = len(l)

    # Initialize curr_sum as
    # value of first element
    # and starting point as 0
    count = start = 0
    curr_sum = l[0]

    # Initialize the index as 1
    index = 1

    # Add elements one by
    # one to curr_sum and
    # if the index exceeds
    # the m, then remove
    # starting element
    # and change the value
    # of index as m-1
    i = 1
    while i <= n:

        # If curr_sum becomes
        # equal to sum, then
        # increment count by 1
        if curr_sum == s and index == m:
            count += 1

        # If index exceeds
        # the m, then remove
        # the starting elements
        while index >= m:
            curr_sum -= l[start]
            start += 1
            index = m - 1

        # Add this element
        # to curr_sum and
        # increment index
        if i < n:
            curr_sum += l[i]
            index += 1
        i += 1

    return count


# Driver's code
l = [1, 2, 1, 3, 2]
s = 3
m = 2

ans = SearchWay(l, s, m)
print(ans)
