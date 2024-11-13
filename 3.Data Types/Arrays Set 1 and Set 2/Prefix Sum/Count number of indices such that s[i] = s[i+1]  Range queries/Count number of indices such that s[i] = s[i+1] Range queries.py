# Python3 program for the given approach

# Function to create prefix array
def preCompute(n, s, pref):
    for i in range(1, n):
        pref[i] = pref[i - 1]
        if s[i - 1] == s[i]:
            pref[i] += 1


# Function to return the result of the query
def query(pref, l, r):
    return pref[r] - pref[l]


if __name__ == "__main__":
    s = "ggggggg"
    n = len(s)

    pref = [0] * n
    preCompute(n, s, pref)

    # Query 1
    l = 1
    r = 2
    print(query(pref, l, r))

    # Query 2
    l = 1
    r = 5
    print(query(pref, l, r))


