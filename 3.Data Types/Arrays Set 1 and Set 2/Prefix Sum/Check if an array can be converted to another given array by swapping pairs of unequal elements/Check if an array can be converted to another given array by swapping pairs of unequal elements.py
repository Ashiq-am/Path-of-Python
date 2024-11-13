# Python 3 program for the above approach

# Function to check if arr1[] can be
# converted to arr2[] by swapping pair
# (i, j) such that i < j and arr[i] is
# 1 and arr[j] is 0
def canMakeEqual(arr1, arr2, N):
    # Stores the differences of prefix
    # sum of arr1 and arr2
    count = 0

    # Stores the count of 1 and
    # zero of arr1
    arr1_one = 0
    arr1_zero = 0

    # Stores the count of 1 and
    # zero of arr2
    arr2_one = 0
    arr2_zero = 0

    # Iterate in the range [0, N - 1]
    for i in range(N):

        # If arr1[i] is 1, then
        # increment arr1_one by one
        if (arr1[i] == 1):
            arr1_one += 1

        # Otherwise increment
        # arr1_zero by one
        elif (arr1[i] == 0):
            arr1_zero += 1

        # If arr2[i] is 1, then
        # increment arr2_one by one
        if (arr2[i] == 1):
            arr2_one += 1

        # Otherwise increment
        # arr2_zero by one
        elif (arr2[i] == 0):
            arr2_zero += 1

    # Check if number of 1s and 0s
    # of arr1 is equal to number of
    # 1s and 0s of arr2 respectievly
    if (arr1_one != arr2_one or arr1_zero != arr2_zero):
        print("No")
        return

    # Iterate over the range [0, N-1]
    for i in range(N):

        # Increment count by differences
        # arr1[i] and arr2[i]
        count = count + (arr1[i] - arr2[i])

        # Check if number of 1's in
        # arr2 are more than arr1 and
        # then print "No"
        if (count < 0):
            print("No")
            return

    # Finally, print "Yes"
    print("Yes")


# Driver Code
if __name__ == '__main__':
    # Given input a
    arr1 = [0, 1, 1, 0]
    arr2 = [0, 0, 1, 1]

    # Size of the array
    N = len(arr1)

    # Function Call
    canMakeEqual(arr1, arr2, N)
