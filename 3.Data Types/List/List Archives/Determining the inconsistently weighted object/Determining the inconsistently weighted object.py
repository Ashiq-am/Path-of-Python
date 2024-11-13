# Python program to determine the
# inconsistently weighted object

# Function to get the difference of two lists
def subt(A, B):
    return list(set(A) - set(B))


# Function to get the intersection of two lists
def intersection(A, B):
    return list(set(A).intersection(set(B)))


# Function to get the intersection of two lists
def union(A, B):
    return list(set(A).union(set(B)))


# Function to find the inconsistently weighted object
def inconsistentlyWeightedObject(N, Q, comparisons):
    # Objects which appear on the heavier side
    heavierObj = [i for i in range(1, N + 1)]

    # Objects which appear on the lighter side
    lighterObj = [i for i in range(1, N + 1)]
    equalObj = []  # Objects which appear in '=' comparisons

    # Objects which don't appear in any comparison
    objectNotCompared = [i for i in range(1, N + 1)]

    for c in comparisons:
        objectNotCompared = subt(objectNotCompared, union(c[0], c[2]))

        if c[1] == '=':
            equalObj = union(equalObj, union(c[0], c[2]))
        elif c[1] == '<':
            # Removing those objects which do
            # not appear on the lighter side
            lighterObj = intersection(lighterObj, c[0])

            # Removing thoe objects which do
            # not appear on the heavier side
            heavierObj = intersection(heavierObj, c[2])
        else:
            # Removing those objects which do
            # not appear on the lighter side
            lighterObj = intersection(lighterObj, c[2])

            # Removing those objects which do
            # not appear on the heavier side
            heavierObj = intersection(heavierObj, c[0])

    L_iwo = subt(union(heavierObj, lighterObj), equalObj)  # Potential candidates

    if len(L_iwo) == 1:
        return L_iwo[0]
    elif not len(L_iwo):
        if len(objectNotCompared) == 1:
            return objectNotCompared[0]
        else:
            return 'Insufficient data'
    else:
        return 'Insufficient data'


# Driver code
N = 6
Q = 3
comparisons = [[[1, 2], '=', [5, 6]], [[1, 2, 3], '>', [4, 5, 6]],
               [[3, 4], '<', [5, 6]]]
print(inconsistentlyWeightedObject(N, Q, comparisons))
