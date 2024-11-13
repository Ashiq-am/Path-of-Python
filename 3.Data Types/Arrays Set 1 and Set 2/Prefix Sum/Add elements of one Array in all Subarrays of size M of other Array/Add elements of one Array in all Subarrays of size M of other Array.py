# python code

# Function to find the final state of arr1[]
def addArr2ToArr1(arr1, arr2, N, M):
    # Iterating through all possible subarrays
    # of size M in arr1[] there will be
    # exactly N - M + 1 subarrays
    for i in range(0, N - M + 1):

        # Iterating through M elements of arr2[]
        # and adding in arr1[]'s 'i'th subarray's
        # 'i + j' th element
        for j in range(0, M):
            arr1[i + j] = arr1[i + j] + arr2[j]

    # Printing finaly array
    for i in range(0, N):
        print(arr1[i], end=" ")
    print()


# Driver program
arr1 = [1, 1, 1, 1, 1]
arr2 = [1, 1, 1]
N = len(arr1)
M = len(arr2)

# Function call for testcase 1
addArr2ToArr1(arr1, arr2, N, M)

arr3 = [10, 11, 12, 13, 14]
arr4 = [10]
N2 = len(arr3)
M2 = len(arr4)

# Function call for testcase 2
addArr2ToArr1(arr3, arr4, N2, M2)

arr5 = [12, 11, 10, 9]
arr6 = [1, 2, 3, 4, 5]
N3 = len(arr5)
M3 = len(arr6)

# Function call for testcase 3
addArr2ToArr1(arr5, arr6, N3, M3)

# This code is contributed by ksam24000
