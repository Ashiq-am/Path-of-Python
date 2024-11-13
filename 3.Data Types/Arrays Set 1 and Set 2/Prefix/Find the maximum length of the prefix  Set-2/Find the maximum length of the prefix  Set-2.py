# Python3 program for the above approach

# Function to find the maximum
# length of the required prefix
def maxPrefixLen(arr, N):
    # Stores the frequency of
    # elements
    a, b = {}, {}

    # Stores the maximum length
    # of the prefix satisfying
    # the conditions
    ans = 1

    # Traverse the array arr[]
    for i in range(N):

        # Stores the count of
        # current element
        curr = 0 if (arr[i] not in a) else a[arr[i]]

        # If curr is not
        # equal to 0
        if (curr != 0):

            # Decrement b[curr]
            # by 1
            b[curr] -= 1

            # If b[curr] is 0
            if (b[curr] == 0):
                # Remove b[curr]
                # from the b
                del b[curr]

        # Update
        a[arr[i]] = a.get(arr[i], 0) + 1
        b[curr + 1] = b.get(curr + 1, 0) + 1

        # If all elements in the
        # prefix are same or if
        # all elements have frequency
        # 1
        if (a[arr[i]] == i + 1 or
                (1 in b) and b[1] == i + 1):

            # Update the value of ans
            ans = max(ans, i + 1)

        # Else if the size of b
        # is 2
        elif (len(b) == 2):
            p = list(b.keys())[0]
            q = list(b.keys())[1]

            freq1 = p
            freq2 = q

            count1 = b[p]
            count2 = b[q]

            # If difference between
            # freq2 and freq1 is
            # equal to 1 and if
            # count2 is equal to 1
            if (freq2 - freq1 == 1 and count2 == 1):

                # Update the value
                # of ans
                ans = max(ans, i + 1)

            # If difference between
            # freq1 and freq2 is
            # equal to 1 and if
            # count1 is equal to 1
            elif (freq1 - freq2 == 1 and count1 == 1):

                # Update the value
                # of ans
                ans = max(ans, i + 1)

            # If freq2 and count2 is 1
            # or freq1 and count1 is 1
            if ((freq2 == 1 and count2 == 1) or
                    (freq1 == 1 and count1 == 1)):
                # Update the value of
                # ans
                ans = max(ans, i + 1)

    # Return ans
    return ans


# Driver Code
if __name__ == '__main__':
    arr = [1, 1, 1, 2, 2, 2, 3,
           3, 3, 4, 4, 4, 5]
    N = len(arr)

    print(maxPrefixLen(arr, N))

# This code is contributed by mohit kumar 29
