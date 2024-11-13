# Python3 implementation of above approach

# Function to check if N
# is a Pangram or not
def numberPangram(N):
    # Stores equivalent string
    # representation of N
    num = str(N)

    # Convert the string to set
    setnum = set(num)

    # If the length of set is 10
    if (len(setnum) == 10):

        # The number is a Pangram
        return True
    else:
        return False


# Driver Code

N = 10239876540022
print(numberPangram(N))
