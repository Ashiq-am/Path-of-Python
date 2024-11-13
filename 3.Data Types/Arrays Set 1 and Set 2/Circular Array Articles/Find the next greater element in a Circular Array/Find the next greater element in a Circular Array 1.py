# Python3 program to demonstrate the use of circular
# array without using extra memory space

# Function to find the Next Greater Element(NGE)
def printNGE(A, n):
    for i in range(n):

        # Initialise k as -1 which is printed when no NGE
        # found
        k = -1
        for j in range(i + 1, n + i):
            if (A[i] < A[j % n]):
                print(A[j % n], end=" ")
                k = 1
                break

        if (k == -1):  # Gets executed when no NGE found
            print("-1 ", end="")


# Given array arr[]
arr = [8, 6, 7]

N = len(arr)

# Function call
printNGE(arr, N)


