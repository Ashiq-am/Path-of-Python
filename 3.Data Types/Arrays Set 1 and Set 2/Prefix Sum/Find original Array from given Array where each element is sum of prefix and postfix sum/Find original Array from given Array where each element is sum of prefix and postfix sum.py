# python3 Algorithm for the above approach

# Function to find the original
# array nums[]
def findOrgArray(arr, N):
    # Total variable stores the sum of
    # elements of arr[]
    total = 0
    for i in arr:
        total += i

    # Sum variable stores the sum of
    # elements of nums[]
    sum = int(total / (N + 1));
    v = []

    # Traversing to find the elements
    # of nums[]
    for i in range(N):
        val = arr[i] - sum
        v.append(val)

    # Returning nums[]
    return v


# Driver Code
if __name__ == "__main__":

    N = 4
    arr = [9, 10, 11, 10]

    v = findOrgArray(arr, N)
    for val in v:
        print(val, end=' ')

# this code is contributed by aditya942003patil
