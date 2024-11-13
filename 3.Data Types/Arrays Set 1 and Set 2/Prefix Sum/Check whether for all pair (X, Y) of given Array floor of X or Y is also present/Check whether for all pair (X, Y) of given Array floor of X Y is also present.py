# Python code to implement the above approach

# Function to check whether X/Y is present or not
def solve(n, c, arr):
    # Creating hash array
    # and prefix sum array
    a = []
    b = []
    a = [0 for i in range(c + 1)]
    b = [0 for i in range(c + 1)]
    for i in range(0, n):
        a[arr[i]] += 1
        b[arr[i]] += 1

    # Performing prefix sum.
    for i in range(0, c + 1):
        a[i] += a[i - 1]

    for i in range(0, c + 1):

        # Taking original array elements
        if b[i] > 0:
            for j in range(i - 1, c + 1, i):

                # If element already exist
                # it will give 1 hence true case
                # if doesnt exist
                # we will move forward
                if b[(j + 1) / i] == 0:

                    # we will take two indices
                    # to check whether item
                    # is present.
                    # If any element is present
                    # between then a[id1]!=ad[id2]
                    id1 = j
                    id2 = j + i
                    id2 = min(id2, c)
                    if a[id1] != a[id2]:
                        return False
        # If all above cases turns true
        return True


# Driver Code
if __name__ == "__main__":
    N = 3
    K = 5
    arr = [1, 2, 5]
    flag = solve(N, K, arr)
    if (flag == True):
        print("Yes")
    else:
        print("No")
