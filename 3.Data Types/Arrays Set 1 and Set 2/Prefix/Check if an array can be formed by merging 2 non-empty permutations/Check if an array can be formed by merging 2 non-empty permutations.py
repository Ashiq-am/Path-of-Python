# Python3 program for above approach
def if_merged_permutations(a, n):
    pre_mex = [1 for i in range(n)]

    # Calculate the mex of the
    # array a[0...i]
    freq = [0 for i in range(n + 1)]

    # Mex of empty array is 1
    mex = 1

    # Calculating the frequency
    # of array elements
    for i in range(n):
        freq[a[i]] += 1
        if freq[a[i]] > 1:
            # In a permutation
            # each element is
            # present one time,
            # So there is no chance
            # of getting permutations
            # for the prefix of
            # length greater than i
            break

        # The current element
        # is the mex
        if a[i] == mex:

            # While mex is present
            # in the array
            while freq[mex] != 0:
                mex += 1
        pre_mex[i] = mex

    suf_mex = [1 for i in range(n)]

    # Calculate the mex of the
    # array a[i..n]
    freq = [0 for i in range(n + 1)]

    # Mex of empty array is 1
    mex = 1

    # Calculating the frequency
    # of array elements
    for i in range(n - 1, -1, -1):
        freq[a[i]] += 1
        if freq[a[i]] > 1:
            # In a permutation each
            # element is present
            # one time, So there is
            # no chance of getting
            # permutations for the
            # suffix of length lesser
            # than i
            break

        # The current element is
        # the mex
        if a[i] == mex:
            # While mex is present
            # in the array
            while freq[mex] != 0:
                mex += 1
        suf_mex[i] = mex

    # Now check if there is atleast
    # one index i such that mex of
    # the prefix a[0..i]= i +
    # 2(0 based indexing) and mex
    # of the suffix a[i + 1..n]= n-i

    for i in range(n - 1):
        if pre_mex[i] == i + 2 and suf_mex[i + 1] == n - i:
            print("YES")
            return
    print("NO")


a = [1, 3, 2, 4, 3, 1, 2]
n = len(a)
if_merged_permutations(a, n)
