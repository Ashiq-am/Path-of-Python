# Python3 program for the above approach
from math import sqrt


# Function to find an index in the
# array having sum of prime numbers
# to its left and right equal
def find_index(arr, N):
    # Stores the maximum value
    # present in the array
    max_value = -10 ** 9

    for i in range(N):
        max_value = max(max_value, arr[i])

    # Stores all positive
    # elements which are <= max_value
    store = {}

    for i in range(1, max_value + 1):
        store[i] = store.get(i, 0) + 1

    # If 1 is present
    if (1 in store):
        # Remove 1
        del store[1]

    # Sieve of Eratosthenes to
    # store all prime numbers which
    # are <= max_value in the Map
    for i in range(2, int(sqrt(max_value)) + 1):
        multiple = 2

        # Erase non-prime numbers
        while ((i * multiple) <= max_value):

            if (i * multiple in store):
                del store[i * multiple]

            multiple += 1

    # Stores the sum of
    # prime numbers from left
    prime_sum_from_left = 0

    # Stores the sum of prime numbers
    # to the left of each index
    first_array = [0] * N

    for i in range(N):

        # Stores the sum of prime numbers
        # to the left of the current index
        first_array[i] = prime_sum_from_left
        if arr[i] in store:
            # Add current value to
            # the prime sum if the
            # current value is prime
            prime_sum_from_left += arr[i]

    # Stores the sum of
    # prime numbers from right
    prime_sum_from_right = 0

    # Stores the sum of prime numbers
    # to the right of each index
    second_array = [0] * N

    for i in range(N - 1, -1, -1):

        # Stores the sum of prime
        # numbers to the right of
        # the current index
        second_array[i] = prime_sum_from_right

        if (arr[i] in store):
            # Add current value to the
            # prime sum if the
            # current value is prime
            prime_sum_from_right += arr[i]

    # Traverse through the two
    # arrays to find the index
    for i in range(N):

        # Compare the values present
        # at the current index
        if (first_array[i] == second_array[i]):
            # Return the index where
            # both the values are same
            return i

    # No index is found.
    return -1


# Driver Code
if __name__ == '__main__':
    # Given array arr[]
    arr = [11, 4, 7, 6, 13, 1, 5]

    # Size of Array
    N = len(arr)

    # Function Call
    print(find_index(arr, N))


