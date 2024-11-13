# python program to calculate prefix sum of 3d array
# Declaring size of the array
L = 4  # Layer
R = 4  # Row
C = 4  # Column


# Calculating prefix
def prefixSum3d(A):
    pre = [[[0 for a in range(C)]
            for b in range(R)]
           for d in range(L)]

    # Step 0:
    pre[0][0][0] = A[0][0][0]

    # Step 1: Filling the first row,column, and pile of ceils.
    # Using prefix sum of 1d array
    for i in range(1, L):
        pre[i][0][0] = pre[i - 1][0][0] + A[i][0][0]

    for i in range(1, R):
        pre[0][i][0] = pre[0][i - 1][0] + A[0][i][0]

    for i in range(1, C):
        pre[0][0][i] = pre[0][0][i - 1] + A[0][0][i]

    # Step 2: Filling the cells of sides(made up using cells)
    # which have common element A[0][0][0].
    # using prefix sum on 2d array
    for k in range(1, L):
        for i in range(1, R):
            pre[k][i][0] = (A[k][i][0] + pre[k - 1][i][0] + pre[k][i - 1][0]
                            - pre[k - 1][i - 1][0])
    for i in range(1, R):
        for j in range(1, C):
            pre[0][i][j] = (A[0][i][j] + pre[0][i - 1][j] + pre[0][i][j - 1]
                            - pre[0][i - 1][j - 1])
    for j in range(1, C):
        for k in range(1, L):
            pre[k][0][j] = (A[k][0][j] + pre[k - 1][0][j] + pre[k][0][j - 1]
                            - pre[k - 1][0][j - 1])

    # Step 3: Filling value in remaining cells using formula
    for k in range(1, L):
        for i in range(1, R):
            for j in range(1, C):
                pre[k][i][j] = (A[k][i][j]

                                + pre[k - 1][i][j]
                                + pre[k][i - 1][j]
                                + pre[k][i][j - 1]

                                - pre[k - 1][i - 1][j]
                                - pre[k][i - 1][j - 1]
                                - pre[k - 1][i][j - 1]

                                + pre[k - 1][i - 1][j - 1])

    # Displaying final prefix sum of array
    for k in range(L):
        print("Layer", k + 1, ":")
        for i in range(R):
            for j in range(C):
                print(pre[k][i][j], end=' ')
            print()
        print()


# Driver program to test above function
A = [
    [[1, 1, 1, 1],  # Layer 1
     [1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 1]],

    [[1, 1, 1, 1],  # Layer 2
     [1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 1]],

    [[1, 1, 1, 1],  # Layer 3
     [1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 1]],

    [[1, 1, 1, 1],  # Layer 4
     [1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 1]]
]

prefixSum3d(A)
