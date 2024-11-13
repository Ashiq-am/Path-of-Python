# Python 3 code to count element with
# values at least x.

# For every query in x[0..q-1], count
# of values greater than or equal to
# query value are printed.
def coutIndices(n, l, r, m, x, q):
    # Start and end store frequencies
    # of all starting and ending points
    start = [0 for i in range(n + 1)]
    End = [0 for i in range(n + 1)]
    for i in range(0, m, 1):
        start[l[i]] += 1
        End[r[i]] += 1

    # Find actual array values
    # after m queries
    compute = [0 for i in range(n + 1)]
    compute[1] = start[1]
    for i in range(1, n + 1, 1):
        compute[i] = (compute[i - 1] +
                      start[i] - End[i - 1])

    # Find frequency of every
    # element in compute[]
    max = compute[0]
    for i in range(len(compute)):
        if (compute[i] > max):
            max = compute[i]

    freq = [0 for i in range(max + 1)]
    for i in range(1, n + 1, 1):
        freq[compute[i]] += 1

    # reverse cumulative sum of the freq
    # array because of atleast value of
    # array indices for each possible x
    i = max - 1
    while (i >= 0):
        freq[i] += freq[i + 1]
        i -= 1

    # Solving queries
    for i in range(0, q, 1):
        print("number of indexes with atleat",
              x[i], "is", end=" ")
        if (x[i] > max):
            print(0)
        else:
            print(freq[x[i]])

        # Driver code


if __name__ == '__main__':
    # Number of elements in an array
    # with all initial 0 values
    n = 7

    # Subarrays that need to be incremented
    l = [1, 2, 1, 5]
    r = [3, 5, 2, 6]

    # Query values
    x = [1, 7, 4, 2]

    m = len(l)
    q = len(x)
    coutIndices(n, l, r, m, x, q)


