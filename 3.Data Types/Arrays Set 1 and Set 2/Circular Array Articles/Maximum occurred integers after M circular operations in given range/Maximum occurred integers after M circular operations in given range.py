# Python3 program for the above approach

# Function to find the maximum
# occurred integer after completing
# all circular operations
def mostvisitedsector(N, A):
    # Stores the highest visit count
    # for any element
    maxVisited = 0

    # Stors the number of times an
    # element is visited
    mp = {}

    # Iterate over the array
    for i in range(0, len(A) - 1):
        start = A[i] % N
        end = A[i + 1] % N

        # Iterate over the range
        # circularly form start to end
        while (start != end):

            # Count number of times an
            # element is visited
            if (start == 0):

                # Increment frequency
                # of N
                if N in mp:
                    mp[N] = mp[N] + 1
                else:
                    mp[N] = 1

                # Update maxVisited
                if (mp[N] > maxVisited):
                    maxVisited = mp[N]

            else:

                # Increment frequency
                # of start
                if start in mp:
                    mp[start] = mp[start] + 1
                else:
                    mp[start] = 1

                # Update maxVisited
                if (mp[start] > maxVisited):
                    maxVisited = mp[start]

            # Increment the start
            start = (start + 1) % N

    # Increment the count for the last
    # visited element
    if A[-1] in mp:
        mp[A[-1]] = mp[A[-1]] + 1

    if (mp[A[-1]] > maxVisited):
        maxVisited = mp[A[-1]]

    # Print most visited elements
    for x in mp:
        if (mp[x] == maxVisited):
            print(x, end=' ')


# Driver Code
if __name__ == '__main__':
    N = 4
    arr = [1, 2, 1, 2]

    # Function Call
    mostvisitedsector(N, arr)
