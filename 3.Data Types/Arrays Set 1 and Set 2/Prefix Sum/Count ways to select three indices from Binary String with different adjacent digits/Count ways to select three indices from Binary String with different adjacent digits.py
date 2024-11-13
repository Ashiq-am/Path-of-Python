# Python3 code to implement the approach

# Function to find the number of ways
def numberOfWays(s):
    n = len(s);

    # Initialize a variable totalZero and
    # totalOne to 0, this will keep track
    # of total number of zeros and ones
    # in the binary string respectively.
    totalZero = 0;
    totalOne = 0;

    # Initialise variable currZero and
    # currOne to 0, this will keep track
    # of number of zeros and ones till
    # ith index.
    currZero = 0;
    currOne = 0;

    # Iterate over the string
    for i in range(n):

        # If the curr digit is zero
        # increment the totalZero by 1
        if (s[i] == '0'):
            totalZero += 1;

        # Otherwise, increment the
        # totalOne by 1
        else:
            totalOne += 1;

    # Initialise a variable result, to
    # keep track of the answer
    result = 0;

    # Iterate over the string
    for i in range(n):

        # If the current digit is 0
        if (s[i] == '0'):

            # Add the value of (number of
            # ones to the left * number
            # of ones to the right)
            result += (currOne * (totalOne - currOne));

            # Increment the count of
            # currZero by 1
            currZero += 1;

        # Otherwise, Add the value of
        # (number of zeros to the left
        # * number of zeros to the right)
        else:
            result += (currZero * (totalZero - currZero));

            # Increment the count of
            # currOnes by 1
            currOne += 1;

    # Finally, return result.
    return result;


# Drivers code
if __name__ == "__main__":
    # First test case
    s = "00110";
    print(numberOfWays(s));

    # Second test case
    s = "11100";
    print(numberOfWays(s));

    # Third test case
    s = "0000";
    print(numberOfWays(s));

    # Fourth test case
    s = "101";
    print(numberOfWays(s));

# This code is contributed by AnkThon
