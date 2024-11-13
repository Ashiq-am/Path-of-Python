# Python3 implementation to Count the
# number of groups having the largest
# size where groups are according
# to the sum of its digits

# Create the dictionary of unique sum
def constDict(n):
    # dictionary that contain
    # unique sum count
    d = {}

    for i in range(1, n + 1):

        # convert each number to string
        s = str(i)

        # make list of number digits
        l = list(s)

        # calculate the sum of its digits
        sum1 = sum(map(int, l))

        if sum1 not in d:
            d[sum1] = 1

        else:
            d[sum1] += 1

    return d


# function to find the
# largest size of group
def countLargest(n):
    d = constDict(n)

    size = 0

    # count of largest size group
    count = 0

    for k, val in d.items():

        if val > size:

            size = val
            count = 1

        elif val == size:

            count += 1

    return count


# Driver Code
n = 13
group = countLargest(n)
print(group)
