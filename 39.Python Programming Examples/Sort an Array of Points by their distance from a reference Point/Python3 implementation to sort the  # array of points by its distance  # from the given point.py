# Python3 implementation to sort the
# array of points by its distance
# from the given point

# Function to sort the array of
# points by its distance from P
def sortArr(arr, n, p):
    # Vector to store the distance
    # with respective elements
    vp = []

    # Storing the distance with its
    # distance in the vector array
    for i in range(n):
        dist = pow((p[0] - arr[i][0]), 2) + pow((p[1] - arr[i][1]), 2)

        vp.append([dist, [arr[i][0], arr[i][1]]])

    # Sorting the array with
    # respect to its distance
    vp.sort()

    # Output
    for i in range(len(vp)):
        print("(", vp[i][1][0], ", ", vp[i][1][1], ") ", sep="", end="")

    # Driver code


arr = [[5, 5], [6, 6], [1, 0], [2, 0], [3, 1], [1, -2]]
n = 6
p = [0, 0]

# Sorting Array
sortArr(arr, n, p)
