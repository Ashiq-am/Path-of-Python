# Function to check if it is possible to
# find 4 integers satisfying the
# given condition
def isPossible(N, A, X, Y, Z):
    # Declaring a set
    S = set()

    # Initializing variable to store
    # cumulative sum
    curr = 0

    # Inserting cumulative sums
    # into the set
    for i in range(N):
        curr += A[i]
        S.add(curr)

    # Iterating through the set
    for it in S:

        # If current element of set
        # satisfies the given condition
        # along with 3 other elements
        # (which are also in set),
        # return true
        if ((it + X) in S
                and (it + X + Y) in S
                and (it + X + Y + Z) in S):
            return True

    # Return false if the iteration
    # completes without getting
    # the required elements
    return False


# Driver code
if __name__ == "__main__":

    N = 10
    X = 5
    Y = 7
    Z = 5
    A = [1, 3, 2, 2, 2, 3, 1, 4, 3, 2]

    # Function call
    answer = isPossible(N, A, X, Y, Z)
    if (answer == True):
        print("YES")

    else:
        print("NO")

# This code is contributed by code_hunt.
