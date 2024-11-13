# Python3 program for the above approach

# Function to compute sum of Bitwise OR
# of each element in arr1[] with all
# elements of the array arr2[]
def Bitwise_OR_sum_i(arr1, arr2, M, N):
    # Declaring an array of
    # size 32 to store the
    # count of each bit
    frequency = [0] * 32

    # Traverse the array arr1[]
    for i in range(N):

        # Current bit position
        bit_position = 0
        num = arr1[i]

        # While num exceeds 0
        while (num):

            # Checks if i-th bit
            # is set or not
            if (num & 1 != 0):
                # Increment the count at
                # bit_position by one
                frequency[bit_position] += 1

            # Increment bit_position
            bit_position += 1

            # Right shift the num by one
            num >>= 1

    # Traverse in the arr2[]
    for i in range(M):
        num = arr2[i]

        # Store the ith bit value
        value_at_that_bit = 1

        # Total required sum
        bitwise_OR_sum = 0

        # Traverse in the range [0, 31]
        for bit_position in range(32):

            # Check if current bit is set
            if (num & 1 != 0):

                # Increment the Bitwise
                # sum by N*(2^i)
                bitwise_OR_sum += N * value_at_that_bit

            else:
                bitwise_OR_sum += (frequency[bit_position] *
                                   value_at_that_bit)

            # Right shift num by one
            num >>= 1

            # Left shift valee_at_that_bit by one
            value_at_that_bit <<= 1

        # Print the sum obtained for ith
        # number in arr1[]
        print(bitwise_OR_sum, end=" ")

    return


# Driver Code

# Given arr1[]
arr1 = [1, 2, 3]

# Given arr2[]
arr2 = [1, 2, 3]

# Size of arr1[]
N = len(arr1)

# Size of arr2[]
M = len(arr2)

# Function Call
Bitwise_OR_sum_i(arr1, arr2, M, N)

# This code is contributed by code_hunt
