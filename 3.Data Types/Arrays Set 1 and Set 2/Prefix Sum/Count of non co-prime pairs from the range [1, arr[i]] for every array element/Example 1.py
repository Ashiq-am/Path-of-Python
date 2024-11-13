# Python3 program for the above approach

# Recursive program to
# return gcd of two numbers
def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


# Function to count the number of
# non co-prime pairs for each query
def countPairs(arr, N):
    # Traverse the array arr[]
    for i in range(0, N):

        # Stores the count of
        # non co-prime pairs
        count = 0

        # Iterate over the range [1,x]
        for x in range(1, arr[i] + 1):

            # Iterate over the range [x,y]
            for y in range(x, arr[i] + 1):

                # If gcd of current pair
                # is greater than 1
                if gcd(x, y) > 1:
                    count += 1

        print(count, end=" ")


# Driver code
if __name__ == '__main__':
    # Given Input
    arr = [5, 10, 20]
    N = len(arr)

    # Function Call
    countPairs(arr, N)

# This code is contributed by MuskanKalra1
