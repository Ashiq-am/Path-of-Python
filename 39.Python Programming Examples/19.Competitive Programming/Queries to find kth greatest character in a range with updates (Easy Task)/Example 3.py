# Python3 Program to implement
# the above approach

# Maximum Size of a String
maxn = 100005

# Fenwick Tree to store the
# frequencies of 26 alphabets
BITree = [[0 for x in range(maxn)]
          for y in range(26)]

# Size of the String.
N = 0


# Function to update Fenwick Tree for
# Character c at index val
def update_BITree(index, C, val):
    while (index <= N):
        # Add val to current node
        # Fenwick Tree
        BITree[ord(C) -
               ord('a')][index] += val

        # Move index to parent node
        # in update View
        index += (index & -index)

    # Function to get sum of


# frequencies of character
# c till index
def sum_BITree(index, C):
    # Stores the sum
    s = 0
    while (index):
        # Add current element of
        # Fenwick tree to sum
        s += BITree[ord(C) -
                    ord('a')][index]

        # Move index to parent node
        # in getSum View
        index -= (index & -index)
    return s


# Function to create
# the Fenwick tree
def buildTree(st):
    for i in range(1,
                   N + 1):
        update_BITree(i,
                      st[i], 1)

    print()


# Function to print the
# kth largest character
# in the range of l to r
def printCharacter(st, l,
                   r, k):
    # Stores the count of
    # characters
    count = 0

    for C in range(ord('z'),
                   ord('a') -
                   1, -1):

        # Calculate frequency of
        # C in the given range
        times = (sum_BITree(r, chr(C)) -
                 sum_BITree(l - 1, chr(C)))

        # Increase count
        count += times

        # If count exceeds K
        if (count >= k):
            # Required character
            # found
            ans = chr(C)
            break

    return ans


# Function to update character
# at pos by character s
def updateTree(st, pos, s):
    # 0 based index system
    index = pos;
    update_BITree(index,
                  st[index], -1)

    st.replace(st[index], s, 1)
    update_BITree(index, s, 1)


# Driver Code
if __name__ == "__main__":
    st = "abcddef"
    N = len(st)

    # Makes the string
    # 1-based indexed
    st = '#' + st

    # Number of queries
    Q = 3

    # Construct the Fenwick Tree
    buildTree(st)

    print(printCharacter(st, 1,
                         2, 2))
    updateTree(st, 4, 'g')
    print(printCharacter(st, 1,
                         5, 4))

# This code is contributed by Chitranayal
