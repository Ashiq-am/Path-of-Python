# returns an array z such that z[i]
# stores length of the longest substring starting
# from i which is also a prefix of s
def z_function(s):
    n = len(s)
    z = [0] * n
    # consider a window [l,r]
    # which matches with prefix of s
    l = 0;
    r = 0
    z[0] = n
    for i in range(1, n):
        # when i<=r, we make use of already computed z
        # value for some smaller index
        if (i <= r):
            z[i] = min(r - i + 1, z[i - l])

        # if i>r nothing matches so we will calculate
        # z[i] using naive way.
        while (i + z[i] < n and s[z[i]] == s[i + z[i]]):
            z[i] += 1
        # update window size
        if (i + z[i] - 1 > r):
            l = i;
            r = i + z[i] - 1

    return z


if __name__ == '__main__':
    s = "abcda"

    n = len(s)

    z = z_function(s)

    # stores the count of
    # Sub-strings of a that
    # are prefix of the same string
    count = 0

    for x in z:
        count += x

    print(count)
