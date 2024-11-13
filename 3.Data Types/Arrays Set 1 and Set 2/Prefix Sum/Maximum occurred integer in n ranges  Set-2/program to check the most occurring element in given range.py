# Python3 program to check the most
# occurring element in given range

# Function that returns the
# maximum element.
def maxOccurring(range1, n):
    # freq array to store the frequency
    freq = [0] * 1000002

    first = 0
    last = 0

    # iterate and mark the hash array
    for i in range(n):
        l = range1[i][0]
        r = range1[i][1]

        # increase the hash array by 1 at L
        freq[l] += 1

        # Decrease the hash array by 1 at R
        freq[r + 1] -= 1
        first = min(first, l)
        last = max(last, r)

    # stores the maximum frequency
    maximum = 0
    element = 0

    # check for the most occurring element
    for i in range(first, last + 1):

        # increase the frequency
        freq[i] = freq[i - 1] + freq[i]

        # check if is more than the
        # previous one
        if (freq[i] > maximum):
            maximum = freq[i]
            element = i
    return element


# Driver code
range1 = [[1, 6], [2, 3],
          [2, 5], [3, 8]]
n = 4

# function call
print(maxOccurring(range1, n))


