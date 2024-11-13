# Python implementation of above approach

from collections import Counter


# Function to check if
# N is a Pangram or not
def numberPangram(N):
    # Stores equivalent string
    # representation of N
    num = str(N)

    # Count frequencies of
    # digits present in N
    frequency = Counter(num)

    # If the length of the
    # dictionary frequency is 10
    if (len(frequency) == 10):

        # The number is a Pangram
        return True
    else:
        return False


# Driver Code

N = 10239876540022
print(numberPangram(N))
